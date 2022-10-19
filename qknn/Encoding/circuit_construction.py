import numpy as np
from Encoding.Amplitude_encoding import Amplitude_Encoding
from qiskit import QuantumCircuit
from typing import List
from qiskit.tools import parallel_map
from quantum_circuits.Swap_test_circuit import Create_Swap_test_Circuit


def _construct_circuit(feature_vector_1: np.ndarray,
                       feature_vector_2: np.ndarray,
                       encoding: Amplitude_Encoding = None) -> QuantumCircuit:
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
                                       test_data: np.ndarray, training_data: np.ndarray, encoding:Amplitude_Encoding) -> List[QuantumCircuit]:
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
