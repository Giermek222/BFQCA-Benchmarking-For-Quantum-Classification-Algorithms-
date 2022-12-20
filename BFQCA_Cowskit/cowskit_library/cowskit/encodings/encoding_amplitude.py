from cowskit.encodings.encoding import Encoding
from cowskit.datasets.dataset import Dataset
from qiskit.circuit.library import StatePreparation
import numpy as np

class AmplitudeEncoding(Encoding):
    def __init__(self, dataset: Dataset = None):
        Encoding.__init__(self, dataset)

        self.state = StatePreparation(dataset.get_example().flatten().tolist())
        self.output_shape = self.state.num_qubits

    def encode(self, value:np.ndarray):
        self.state = StatePreparation(value.flatten().tolist())
        return self.state

