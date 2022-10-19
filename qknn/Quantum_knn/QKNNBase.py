from typing import List, Dict, Union

import numpy as np
import logging

from qiskit import QuantumCircuit
from qiskit.result import Result
from qiskit.utils import QuantumInstance

from Encoding import Amplitude_encoding

logger = logging.getLogger(__name__)


class QKNN_Base:
    def __init__(self,
                 n_neighbors: int = 3,
                 encoding: Amplitude_encoding = None,
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

    def fit(self, training_parameters, training_labels):
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
        all_counts = results.get_counts()

        fidelities = np.empty(
            shape=(test_size, train_size)
        )

        for i, counts in enumerate(all_counts):
            fidelity = self._compute_fidelity(counts)
            # the i-th subarray of the ndarray `fidelities` contains
            # the values that we will use for the majority voting to
            # predict the label of the i-th test input data
            fidelities[i // train_size][i % train_size] = fidelity

        return fidelities
