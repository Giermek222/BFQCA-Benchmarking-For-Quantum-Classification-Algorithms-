import qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import ZFeatureMap
from qiskit_machine_learning.algorithms.classifiers import NeuralNetworkClassifier
from qiskit_machine_learning.neural_networks import EstimatorQNN
from qiskit.algorithms.optimizers.adam_amsgrad import ADAM

import numpy as np

from cowskit.models.model import Model
from cowskit.datasets.dataset import Dataset
from cowskit.encodings.encoding import Encoding
from cowskit.utils.decorators import *

class VariationalModel(Model):
    def __init__(self, dataset: Dataset = None, encoding: Encoding = None, depth: int = 1, learning_rate = 0.0001) -> None:
        self.dataset = dataset
        self.encoding = encoding

        self.n_qubits = self.encoding.output_shape
        self.all_qubits = list(range(0, self.n_qubits))

        self.depth = depth

        self.learning_rate = learning_rate

        assert(self.n_qubits <= 32)

        self.register = QuantumRegister(self.encoding.output_shape, 'q')
        self.output = ClassicalRegister(self.encoding.output_shape, 'c')
        self.circuit = QuantumCircuit(self.n_qubits + 1) # + 1 bcoz encoding?
        
        self.build_circuit()
        
    def infer(self):
        def one_iteration(params = None, s = 0):
            encoded_value = self.encoding.encode(value)
            #self.register._bits = encoded_value
            self.circuit.append(encoded_value, self.all_qubits)
            if params is None:
                updated_params = self.build_circuit(params, s = s)
            else:
                updated_params = self.build_circuit(params, s = s)
            self.circuit.measure(self.all_qubits, self.output)

            return updated_params, self.loss(label, self.output)

        params, _ = one_iteration()
        for value, label in iter(self.dataset):
            for i in range(len(params)):
                s = 0.0001
                _, loss_s_positive = one_iteration(params, s = s)
                _, loss_s_negative = one_iteration(params, s = -s)

                gradient = loss_s_positive - loss_s_negative
                params[i] += self.learning_rate * gradient


    def build_circuit(self, old_params, s = 0):        
        params = []
        param_idx = 0
        for i in range(self.depth):
            if old_params is None:
                param1 = np.random.rand()
                param2 = np.random.rand()
                param3 = np.random.rand()
            else:
                param1 = old_params[param_idx] + s
                param2 = old_params[param_idx+1] + s
                param3 = old_params[param_idx+2] + s
                param_idx+=3

            self.circuit.rx(param1, self.all_qubits)
            self.circuit.ry(param2, self.all_qubits)
            self.circuit.rz(param3, self.all_qubits)

            params.append(param1)
            params.append(param2)
            params.append(param3)

            for j in range(self.n_qubits):
                self.circuit.cnot(j, j+1)
            self.circuit.cnot(self.n_qubits - 1, 0)

        return params


    def loss(self, label, output):
        return ((label - output) ** 2).mean(axis=None)

