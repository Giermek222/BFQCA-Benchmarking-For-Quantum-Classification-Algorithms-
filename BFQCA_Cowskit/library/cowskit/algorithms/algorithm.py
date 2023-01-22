import numpy as np
from cowskit.datasets import Dataset
from cowskit.utils import get_shape_size
class Algorithm:
    def __init__(self, dataset: Dataset = None) -> None:
        self.dataset = dataset

    def train(self, X: np.ndarray, Y: np.ndarray) -> None:
        raise Exception("Unimplemented 'train' function in custom algorithm.")

    def predict(self, X: np.ndarray) -> np.ndarray:
        raise Exception("Unimplemented 'predict' function in custom algorithm.")

    # ======================== INTERNAL FUNCTIONS ========================
    def train_safe(self, X: np.ndarray, Y: np.ndarray):
        X = X.reshape((X.shape[0], get_shape_size(X)))
        Y = Y.reshape((Y.shape[0], get_shape_size(Y)))

        self.train(X, Y)

    def predict_safe(self, X: np.ndarray, num_classes: int):
        X = X.reshape((X.shape[0], get_shape_size(X)))

        Y_pred = self.predict(X)

        Y_pred = Y_pred.reshape((X.shape[0], num_classes))
        return Y_pred

    def get_input_size(self):
        return self.dataset.get_input_size()

    def get_output_size(self):
        return self.dataset.get_output_size()

