import qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from cowskit.datasets.dataset import Dataset
from cowskit.algorithms.algorithm import Algorithm
from cowskit.encodings.encoding import Encoding

class Model(Algorithm):
    def __init__(self) -> None:
        Algorithm.__init__(self)
