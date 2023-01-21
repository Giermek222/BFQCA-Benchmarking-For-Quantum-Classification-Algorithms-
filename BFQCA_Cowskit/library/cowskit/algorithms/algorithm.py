import numpy as np
class Algorithm:
    def __init__(self) -> None:
        pass

    def train(self, X: np.ndarray, Y: np.ndarray) -> None:
        raise Exception("Unimplemented 'train' function in custom algorithm.")

    def predict(self, X: np.ndarray) -> np.ndarray:
        raise Exception("Unimplemented 'predict' function in custom algorithm.")

