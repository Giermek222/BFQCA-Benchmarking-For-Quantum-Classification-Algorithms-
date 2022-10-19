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
from Encoding.circuit_construction import _construct_circuits_from_test_data, _construct_circuit


class QKNeighborsClassifier(ClassifierMixin, QKNN_Base):
    r"""
    The Quantum K-Nearest Neighbors algorithm for classification

    Note:
        The naming conventions follow the KNeighborsClassifier from
        sklearn.neighbors

    Example:

        Classify data using the Iris dataset.

        ..  jupyter-execute::

            import numpy as np
            from qlearnkit.algorithms import QKNeighborsClassifier
            from qlearnkit.encodings import AmplitudeEncoding
            from qiskit import BasicAer
            from qiskit.utils import QuantumInstance, algorithm_globals
            from sklearn.datasets import load_iris
            from sklearn.model_selection import train_test_split

            seed = 42
            algorithm_globals.random_seed = seed

            quantum_instance = QuantumInstance(BasicAer.get_backend('qasm_simulator'),
                                               shots=1024,
                                               optimization_level=1,
                                               seed_simulator=seed,
                                               seed_transpiler=seed)

            encoding_map = AmplitudeEncoding(n_features=2)

            # Use iris data set for training and test data
            X, y = load_iris(return_X_y=True)

            X = np.asarray([x[0:2] for x, y_ in zip(X, y) if y_ != 2])
            y = np.asarray([y_ for x, y_ in zip(X, y) if y_ != 2])

            qknn = QKNeighborsClassifier(
                n_neighbors=3,
                quantum_instance=quantum_instance,
                encoding_map=encoding_map
            )

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=seed)
            qknn.fit(X_train, y_train)

            print(f"Testing accuracy: "
                  f"{qknn.score(X_test, y_test):0.2f}")

    """

    def __init__(self,
                 n_neighbors: int = 3,
                 encoding_map: Optional[Amplitude_Encoding] = None,
                 quantum_instance: Optional[Union[QuantumInstance, Backend]] = None):
        """
        Creates a QKNeighborsClassifier Object

        Args:
            n_neighbors:
                number of neighbors participating in the
                majority vote

            encoding_map:
                map to classical data to quantum states.
                This class does not impose any constraint on it.

            quantum_instance:
                the quantum instance to set. Can be a
                :class:`~qiskit.utils.QuantumInstance`, a :class:`~qiskit.providers.Backend`
                or a :class:`~qiskit.providers.BaseBackend`

        """
        super().__init__(n_neighbors, encoding_map, quantum_instance)

    def _majority_voting(self,
                         y_train: np.ndarray,
                         fidelities: np.ndarray) -> np.ndarray:
        r"""
        Performs the classical majority vote procedure of the
        K-Nearest Neighbors classifier with the :math:`k` nearest to
        determine class
        Args:
            y_train: the train labels
            fidelities: the list ``F`` of fidelities used as a measure of
                        distance

        Returns:
            a list of predicted labels for the test data
        Raises:
              ValueError if :math:`\exists f \in F \ t.c. f \notin [0, 1]`, assuming
                a tolerance of `0.2`
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
        """Predict the labels of the provided data."""
        if self.training_parameters is None:
            raise NotFittedError(
                "This QKNeighborsClassifier instance is not fitted yet. "
                "Call 'fit' with appropriate arguments before using "
                "this estimator.")

        circuits = _construct_circuits_from_test_data(X_test, self.training_parameters, self.encoding)
        results = self.execute(circuits)
        # the execution results are employed to compute
        # fidelities which are used for the majority voting
        fidelities = self._get_fidelities(results, len(X_test))

        return self._majority_voting(self.training_labels, fidelities)
