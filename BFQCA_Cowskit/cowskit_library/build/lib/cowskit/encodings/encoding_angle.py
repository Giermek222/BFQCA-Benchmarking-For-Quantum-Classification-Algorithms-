from cowskit.encodings.encoding import Encoding
from cowskit.datasets.dataset import Dataset
from qiskit.circuit.library import StatePreparation
from qiskit import QuantumCircuit
import numpy as np

class AngleEncoding(Encoding):
    def __init__(self, dataset: Dataset = None):
        Encoding.__init__(self, dataset)

        example = dataset.get_example().flatten().tolist()
        self.state = QuantumCircuit(len(example))
        self.output_shape = len(example)

    def encode(self, value:np.ndarray):
        values = value.flatten().tolist()

        for idx, value_as_theta in enumerate(values):
            # TODO optimize to use more angles for 3-float values
            self.state.rx(value_as_theta, idx)

        return self.state

