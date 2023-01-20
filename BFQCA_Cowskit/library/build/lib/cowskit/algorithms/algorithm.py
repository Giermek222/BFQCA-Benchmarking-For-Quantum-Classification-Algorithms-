import numpy as np
class Algorithm:
    def __init__(self) -> None:
        self.input_size = None
        self.output_size = None


    def train(self, X: np.ndarray, Y: np.ndarray) -> None:
        raise Exception("Unimplemented 'train' function in custom algorithm.")

    def predict(self, X: np.ndarray) -> np.ndarray:
        raise Exception("Unimplemented 'predict' function in custom algorithm.")

    def get_input_size(self):
        return self.input_size

    def get_output_size(self):
        return self.output_size

