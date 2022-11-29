import qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from cowskit.datasets.dataset import Dataset
from cowskit.encodings.encoding import Encoding
from cowskit.utils.decorators import *

class Model:
    def __init__(self, dataset: Dataset = None, encoding: Encoding = None) -> None:
        self.dataset = dataset
        self.encoding = encoding

        self.register = QuantumRegister(self.encoding.output_shape, 'q')
        self.output = ClassicalRegister(self.encoding.output_shape, 'c')
        self.circuit = QuantumCircuit(self.register, self.output)
        
        self.all_qubits = list(range(0, self.encoding.output_shape))
        #self.build_circuit()
        
    def infer(self):

        for value, label in iter(self.dataset):
            encoded_value = self.encoding.encode(value)
            #self.register._bits = encoded_value
            self.circuit.append(encoded_value, self.all_qubits)
            self.build_circuit()
            self.circuit.measure(self.all_qubits, self.output)
            
    @VirtualHandle
    def build_circuit(self):
        pass
        
