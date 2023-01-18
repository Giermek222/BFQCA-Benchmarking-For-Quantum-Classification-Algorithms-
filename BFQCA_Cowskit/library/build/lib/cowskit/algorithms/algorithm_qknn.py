import numpy as np

from qiskit.providers import Backend
from qiskit.utils import QuantumInstance
from qiskit.result import Result
from qiskit import QuantumCircuit, BasicAer

from typing import Optional, Union, Dict, List
from sklearn.base import ClassifierMixin
import scipy.stats as stats

from qiskit import QuantumCircuit
from typing import List
from qiskit.tools import parallel_map
from cowskit.encodings import AmplitudeEncoding

import logging
logger = logging.getLogger(__name__)

class QKNN_Base:
    def __init__(self,
                 n_neighbors: int = 3,
                 encoding: AmplitudeEncoding = None,
                 quantum_instance: QuantumInstance = None):
        """
        :param n_neighbors: number of neighbours that the algorithm will compare new data with
        :param encoding: class encoding classical data into quantum vector. Only Amplitude Neocding is currently supported
        :param quantum_instance: Quantum Instance to run quantum gates on
        """
        self.encoding = encoding
        self.quantum_instance = quantum_instance
        self.n_neighbors = n_neighbors
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

    def __init__(self,
                 n_neighbors: int = 3,
                 encoding_map: Optional[AmplitudeEncoding] = None,
                 quantum_instance: Optional[Union[QuantumInstance, Backend]] = None):

        
        quantum_instance = QuantumInstance(BasicAer.get_backend('qasm_simulator'),
                            shots=1024,
                            optimization_level=1)
        super().__init__(n_neighbors, encoding_map, quantum_instance)

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

        return self._majority_voting(self.training_labels, fidelities)


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
