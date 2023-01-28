import numpy as np

from qiskit.utils import QuantumInstance
from qiskit.result import Result
from qiskit import QuantumCircuit, BasicAer, QuantumRegister

from typing import Union, Dict, List
from sklearn.base import ClassifierMixin
import scipy.stats as stats

from qiskit import QuantumCircuit
from typing import List
from qiskit.tools import parallel_map
from cowskit.algorithms import Algorithm
from cowskit.datasets import Dataset
from cowskit.utils import add_quantum_padding, remove_quantum_padding

class AmplitudeEncoding:
    def __init__(self, n_features: int = 2):
        n_qubits = np.log2(n_features)
        if not n_qubits.is_integer():
            n_qubits = np.ceil(n_qubits)
        elif n_qubits == 0:
            n_qubits = 1

        self.num_qubits = int(n_qubits)
        self.num_features = n_features

    def _check_feature_vector(self, x):
        if len(x) != self.num_features:
            raise ValueError(f"Expected features dimension "
                            f"{self.num_features}, but {len(x)} was passed")

    def construct_circuit(self, x) -> QuantumCircuit:
        def encode(classical_data):
            norm = np.linalg.norm(classical_data)
            if norm == 0:
                norm = 1
            # should I also round it 3/4 decimals?
            normalised_vector = classical_data / norm
            return normalised_vector

        self._check_feature_vector(x)
        if self.num_features % 2 != 0:
            # if not power of 2, pad with zeros
            x = np.pad(x, (0, (1 << self.num_qubits) - len(x)))

        state_vector = encode(x)

        q = QuantumRegister(self.num_qubits)
        qc = QuantumCircuit(q)
        qc.initialize(state_vector, [q[i] for i in range(self.num_qubits)])

        qc.data = [d for d in qc.data if d[0].name != "reset"]
        return qc

class KNearestNeighbors(ClassifierMixin, Algorithm):

    def __init__(self, dataset: Dataset = None):
        """
        :param n_neighbors: number of neighbours that the algorithm will compare new data with
        :param encoding: class encoding classical data into quantum vector. Only Amplitude Neocding is currently supported
        :param quantum_instance: Quantum Instance to run quantum gates on
        """
        Algorithm.__init__(self, dataset)
        self.encoding = None
        self.n_neighbors = 3
        self.training_parameters = np.asarray([])
        self.training_labels = np.asarray([])
        self.quantum_instance = QuantumInstance(BasicAer.get_backend('qasm_simulator'),
                            shots=1024,
                            optimization_level=1)
        
        self.x_pad_amount = 0
        self.y_pad_amount = 0

    def train(self, X: np.ndarray, Y: np.ndarray):
        self.training_parameters, self.x_pad_amount = add_quantum_padding(X)
        self.training_labels, self.y_pad_amount = add_quantum_padding(Y)
        self.encoding = AmplitudeEncoding(self.training_parameters.shape[1])

    def predict(self, X_test: np.ndarray) -> np.ndarray:

        X_test, _ = add_quantum_padding(X_test)

        circuits = []

        def _construct_circuit(feature_vector_1: np.ndarray, feature_vector_2: np.ndarray, encoding: AmplitudeEncoding = None):
            encoded_data1 = encoding.construct_circuit(feature_vector_1)
            encoded_data2 = encoding.construct_circuit(feature_vector_2)
            return SwaptestCircuit(encoded_data1, encoded_data2)

        for i, test_point in enumerate(X_test):
            circuits_line = parallel_map(
                _construct_circuit,
                self.training_parameters,
                task_args=[test_point,
                        self.encoding]
            )
            circuits = circuits + circuits_line

        results = self.quantum_instance.execute(circuits)
        fidelities = self._get_fidelities(results, len(X_test))
        Y_out = self._majority_voting(self.training_labels, fidelities)
        if len(Y_out.shape) == 1:
            N = X_test.shape[0]
            Y_out = Y_out.reshape(N, Y_out.shape[0]//N)
        Y_out = remove_quantum_padding(Y_out, self.y_pad_amount)
        return Y_out

    def _majority_voting(self,
                         y_train: np.ndarray,
                         fidelities: np.ndarray) -> np.ndarray:

        def _kneighbors(y_train: np.ndarray,
                fidelities: np.ndarray,
                n_neighbours):

            if np.any(fidelities < -0.2) or np.any(fidelities > 1.2):
                raise ValueError("Detected fidelities values not in range 0<=F<=1:"
                                f"{fidelities[fidelities < -0.2]}"
                                f"{fidelities[fidelities > 1.2]}")

            indices_of_sorted_fidelities = np.argsort(fidelities)
            n_queries, _ = fidelities.shape
            if(len(indices_of_sorted_fidelities) > n_neighbours):
                if n_queries == 1:
                    indices_of_sorted_fidelities = indices_of_sorted_fidelities[n_neighbours:]
                else:
                    indices_of_sorted_fidelities = indices_of_sorted_fidelities[:, -n_neighbours:]

            sorted_labels = y_train[indices_of_sorted_fidelities]

            return sorted_labels

        k_nearest = _kneighbors(y_train, fidelities, self.n_neighbors)
        n_queries = self.training_parameters.shape[0]
        if n_queries == 1:
            labels, _ = stats.mode(k_nearest, keepdims=True)
        else:
            labels, _ = stats.mode(k_nearest, axis=1, keepdims=True)

        return labels.real.flatten()

    def _compute_fidelity(self, counts: Dict[str, int]):

        counts_0 = counts.get('0', 0)
        counts_1 = counts.get('1', 1)
        # squared fidelity
        f_2 = np.abs(counts_0 - counts_1) / self.quantum_instance.run_config.shots
        return np.sqrt(f_2)

    def _get_fidelities(self,
                        results: Result,
                        test_size: int) -> np.ndarray:
        """
        :param results: results from the simulation
        :param test_size: size of test data
        :return: np.ndarray with fidelities of each test data point
        """
        train_size = self.training_parameters.shape[0]
        all_counts = results.get_counts()  # List[Dict(str, int)]

        fidelities = np.empty(
            shape=(test_size, train_size)
        )

        for i, (counts) in enumerate(all_counts):
            fidelity = self._compute_fidelity(counts)
            # the i-th subarray of the ndarray `fidelities` contains
            # the values that we will use for the majority voting to
            # predict the label of the i-th test input data
            fidelities[i // train_size][i % train_size] = fidelity

        return fidelities
class SwaptestCircuit(QuantumCircuit):

    def __init__(self,
                 qc_state_1: QuantumCircuit,
                 qc_state_2: QuantumCircuit,
                 name: str = None):

        def Create_Single_Circuit(qc_alpha: QuantumCircuit, qc_beta: QuantumCircuit) -> QuantumCircuit:
            qc = QuantumCircuit(qc_alpha.num_qubits + qc_beta.num_qubits + 1, 1)

            alpha_qubit_names = [i + 1 for i in range(qc_alpha.num_qubits)]
            beta_qubit_names = [i + qc_alpha.num_qubits + 1 for i in range(qc_alpha.num_qubits)]

            qc.compose(qc_alpha, alpha_qubit_names, inplace=True)
            qc.compose(qc_beta, beta_qubit_names, inplace=True)

            return qc

        n_total = qc_state_1.num_qubits + qc_state_2.num_qubits
        super().__init__(n_total + 1, 1, name=name)

        self.compose(Create_Single_Circuit(qc_state_1, qc_state_2), inplace=True)

        # first apply hadamard
        self.h(0)
        # then perform controlled swaps
        for alpha_qubit in range(2):
            self.cswap(0, alpha_qubit + 1, 1 + alpha_qubit + 2)
        # eventually reapply hadamard
        self.h(0)

        # self.barrier()
        # measure
        self.measure(0, 0)
