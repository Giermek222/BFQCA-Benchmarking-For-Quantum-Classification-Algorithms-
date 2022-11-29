from sklearn.exceptions import NotFittedError

import logging
import numpy as np

from qiskit.providers import Backend
from qiskit.utils import QuantumInstance

from typing import Optional, Union
from sklearn.base import ClassifierMixin
import scipy.stats as stats

from Quantum_knn.QKNNBase import QKNN_Base

from Encoding.Amplitude_encoding import Amplitude_Encoding

logger = logging.getLogger(__name__)
from Quantum_knn.k_nearest_neighbours_helper import _kneighbors
from Encoding.circuit_construction import _construct_circuits_from_test_data


class QKNeighborsClassifier(ClassifierMixin, QKNN_Base):

    def __init__(self,
                 n_neighbors: int = 3,
                 encoding_map: Optional[Amplitude_Encoding] = None,
                 quantum_instance: Optional[Union[QuantumInstance, Backend]] = None):
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
            labels, _ = stats.mode(k_nearest)
        else:
            labels, _ = stats.mode(k_nearest, axis=1)

        # eventually flatten the np.ndarray
        # returned by stats.mode
        print(f"predicted values are {labels.real.flatten()}")
        return labels.real.flatten()

    def predict(self,
                X_test: np.ndarray) -> np.ndarray:
        circuits = _construct_circuits_from_test_data(X_test, self.training_parameters, self.encoding)
        results = self.execute(circuits)
        # the execution results are employed to compute
        # fidelities which are used for the majority voting
        fidelities = self._get_fidelities(results, len(X_test))

        return self._majority_voting(self.training_labels, fidelities)
