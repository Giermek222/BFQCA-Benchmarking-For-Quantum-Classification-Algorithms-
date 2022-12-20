import numpy as np
from qiskit import QuantumCircuit
from typing import List
from qiskit.tools import parallel_map
from cowskit.encodings import AmplitudeEncoding

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