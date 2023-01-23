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

class AmplitudeEncoding:
    """
    class containing logic form encoding classical data to normalised quantum vectors.
    """

    def __init__(self, n_features: int = 2):
        # in n qubits we can store 2^n features
        n_qubits = np.log2(n_features)
        if not n_qubits.is_integer():
            # if number of qubits is not a positive
            # power of 2, an extra qubit is needed
            n_qubits = np.ceil(n_qubits)
        elif n_qubits == 0:
            # in this scenario, n_features = 1
            # then we need 1 qubit
            n_qubits = 1

        self.num_qubits = int(n_qubits)
        self.num_features = n_features

    def _check_feature_vector(self, x):
        if len(x) != self.num_features:
            raise ValueError(f"Expected features dimension "
                             f"{self.num_features}, but {len(x)} was passed")

    def construct_circuit(self, x) -> QuantumCircuit:
        """
        :param x: data that we want to encode
        :return:
        """
        self._check_feature_vector(x)
        if self.num_features % 2 != 0:
            # if not power of 2, pad with zeros
            x = np.pad(x, (0, (1 << self.num_qubits) - len(x)))

        state_vector = self.encode(x)

        q = QuantumRegister(self.num_qubits)
        qc = QuantumCircuit(q)
        qc.initialize(state_vector, [q[i] for i in range(self.num_qubits)])

        qc.data = [d for d in qc.data if d[0].name != "reset"]
        return qc

    def encode(self, classical_data):
        """
        Args:
            classical_data as a numpy array
        Returns:
            return normalised vector of qubits
        """
        norm = np.linalg.norm(classical_data)
        if norm == 0:
            norm = 1
        # should I also round it 3/4 decimals?
        normalised_vector = classical_data / norm
        return normalised_vector

class QKNN_Base(Algorithm):
    def __init__(self, dataset: Dataset = None):
        """
        :param n_neighbors: number of neighbours that the algorithm will compare new data with
        :param encoding: class encoding classical data into quantum vector. Only Amplitude Neocding is currently supported
        :param quantum_instance: Quantum Instance to run quantum gates on
        """
        Algorithm.__init__(self, dataset)
        self.encoding = AmplitudeEncoding(self.dataset.get_input_size())
        self.quantum_instance = None
        self.n_neighbors = 3
        self.training_parameters = np.asarray([])
        self.training_labels = np.asarray([])


    def train(self, training_parameters, training_labels):
        """
        :param training_parameters: data that the algorithm will learn on
        :param training_labels: labels that the algorithm will use to categorize training data
        :return: nothing. it just sets data as parameter of class
        """
        self.training_parameters = np.asarray(training_parameters)
        self.training_labels = np.asarray(training_labels)

    def execute(
            self, quantum_circuit: Union[QuantumCircuit, List[QuantumCircuit]]
    ) -> Result:
        """
        :param quantum_circuit: circuit to be executed
        """
        result = self.quantum_instance.execute(quantum_circuit)
        return result

    def _compute_fidelity(self, counts: Dict[str, int]):
        """
        :param counts: dictionary of 0s and 1s
        :return: calculated fidelity
        """
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

class KNearestNeighbors(ClassifierMixin, QKNN_Base):

    def __init__(self, dataset: Dataset = None):

        QKNN_Base.__init__(self, dataset)
        self.quantum_instance = QuantumInstance(BasicAer.get_backend('qasm_simulator'),
                            shots=1024,
                            optimization_level=1)

    def _majority_voting(self,
                         y_train: np.ndarray,
                         fidelities: np.ndarray) -> np.ndarray:

        """
        calculate which class test case should belong into

        :param y_train:
        :param fidelities:
        :return:
        """

        k_nearest = _kneighbors(y_train, fidelities, self.n_neighbors)
        # getting most frequent values in `k_nearest`
        # in a more efficient way than looping and
        # using, for instance, collections.Counter
        n_queries = self.training_parameters.shape[0]
        if n_queries == 1:
            # case of 1D array
            labels, _ = stats.mode(k_nearest, keepdims=True)
        else:
            labels, _ = stats.mode(k_nearest, axis=1, keepdims=True)

        # eventually flatten the np.ndarray
        # returned by stats.mode
        return labels.real.flatten()

    def predict(self,
                X_test: np.ndarray) -> np.ndarray:
        
        circuits = _construct_circuits_from_test_data(X_test, self.training_parameters, self.encoding)
        results = self.execute(circuits)
        # the execution results are employed to compute
        # fidelities which are used for the majority voting
        fidelities = self._get_fidelities(results, len(X_test))
        Y_out = self._majority_voting(self.training_labels, fidelities)
        return Y_out


def Create_Single_Circuit(qc_alpha: QuantumCircuit, qc_beta: QuantumCircuit) -> QuantumCircuit:
    qc = QuantumCircuit(qc_alpha.num_qubits + qc_beta.num_qubits + 1, 1)

    alpha_qubit_names = [i + 1 for i in range(qc_alpha.num_qubits)]
    beta_qubit_names = [i + qc_alpha.num_qubits + 1 for i in range(qc_alpha.num_qubits)]

    qc.compose(qc_alpha, alpha_qubit_names, inplace=True)
    qc.compose(qc_beta, beta_qubit_names, inplace=True)

    return qc


def Create_Swap_test_Circuit(qc_alpha: QuantumCircuit, qc_beta: QuantumCircuit) -> QuantumCircuit:
    # qc = Create_Single_Circuit(qc_alpha, qc_beta)
    #
    # #     add Hadamarrd gates and Fredkin (cswap) gates
    # qc.h(0)
    # qubits_len = qc_alpha.num_qubits
    # if not qubits_len == qc_beta.num_qubits:
    #     raise ValueError(
    #         f"quantum circuits provided into Swap_1 Test Gate must be equal length. Got alpha with {qc_alpha.num_qubits} qubits, beta with {qc_beta.num_qubits} qubits")
    # for alpha_qubit in range(qubits_len):
    #     qc.cswap(0, alpha_qubit+1, alpha_qubit + qubits_len+1)
    #
    # qc.barrier()
    # # measure top qubit
    # qc.measure(0, 0)

    return SwaptestCircuit(qc_alpha, qc_beta)


class SwaptestCircuit(QuantumCircuit):

    def __init__(self,
                 qc_state_1: QuantumCircuit,
                 qc_state_2: QuantumCircuit,
                 name: str = None):
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

        self.barrier()
        # measure
        self.measure(0, 0)

def _construct_circuit(feature_vector_1: np.ndarray,
                       feature_vector_2: np.ndarray,
                       encoding: AmplitudeEncoding = None) -> QuantumCircuit:
    """

    :param feature_vector_1: feature vector of classical data
    :param feature_vector_2: feature vector of calissical data
    :param encoding: Amplitude encoding
    :return:
    """
    encoded_data1 = encoding.construct_circuit(feature_vector_1)
    encoded_data2 = encoding.construct_circuit(feature_vector_2)

    return Create_Swap_test_Circuit(encoded_data1, encoded_data2)


def _construct_circuits_from_test_data(
                                       test_data: np.ndarray, training_data: np.ndarray, encoding:AmplitudeEncoding) -> List[QuantumCircuit]:
    """
    :param test_data: test data to be classified
    :return:
    """

    circuits = []
    # loop thorugh test data and calculate distances
    for i, test_point in enumerate(test_data):
        circuits_line = parallel_map(
            _construct_circuit,
            training_data,
            task_args=[test_point,
                       encoding]
        )
        circuits = circuits + circuits_line

    return circuits

def _kneighbors(y_train: np.ndarray,
                fidelities: np.ndarray,
                n_neighbours,
                *,
                return_indices=False):

    if np.any(fidelities < -0.2) or np.any(fidelities > 1.2):
        raise ValueError("Detected fidelities values not in range 0<=F<=1:"
                         f"{fidelities[fidelities < -0.2]}"
                         f"{fidelities[fidelities > 1.2]}")

    # first sort neighbors
    indices_of_sorted_fidelities = np.argsort(fidelities)

    # extract indices according to number of neighbors
    # and dimension
    n_queries, _ = fidelities.shape
    if n_queries == 1:
        indices_of_sorted_fidelities = indices_of_sorted_fidelities[n_neighbours:]
    else:
        indices_of_sorted_fidelities = indices_of_sorted_fidelities[:, -n_neighbours:]

    sorted_labels = y_train[indices_of_sorted_fidelities]

    if return_indices:
        return sorted_labels, indices_of_sorted_fidelities
    else:
        return sorted_labels
