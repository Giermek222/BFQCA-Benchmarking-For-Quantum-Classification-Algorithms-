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

class ConvolutionalModel(Model):
    def __init__(self, dataset: Dataset = None, encoding: Encoding = None) -> None:
        self.dataset = dataset
        self.encoding = encoding

        self.n_qubits = self.encoding.output_shape
        self.all_qubits = list(range(0, self.n_qubits))

        assert(self.n_qubits <= 32)

        self.register = QuantumRegister(self.n_qubits, 'q')
        self.output = ClassicalRegister(self.n_qubits, 'c')

        self.feature_map = ZFeatureMap(self.n_qubits)  # This should be encoder
        self.instruction_set = QuantumCircuit(self.n_qubits, name = "Conv Network Instruction Set")

        self.circuit = QuantumCircuit(self.register, self.output)
        
        self.build_circuit()
        
    def infer(self):

        self.network = EstimatorQNN(
            circuit=self.circuit.decompose(),
            input_params=self.feature_map.parameters,
            weight_params=self.instruction_set.parameters,
            observables=self.output
        )

        self.classifier = NeuralNetworkClassifier(
            self.network,
            optimizer=ADAM(maxiter=200), 
            initial_point=self.register,  # ? should be array
        )

        for value, label in self.dataset:
            #Logger.info(f"Processing pair")
            self.classifier.fit(value, label)

    def predict(self, value: np.ndarray):
        return self.classifier.predict(value)
            
    def build_circuit(self):

        n_qubits = self.n_qubits
        layer = 0
        while(n_qubits != 1):
            # Convolutional & Pooling Layer
            layer += 1
            self.instruction_set.compose(self.conv_layer(n_qubits, f"с{layer}"), list(range(n_qubits)), inplace=True)
            self.instruction_set.compose(self.pool_layer(list(range(0,n_qubits//2)), list(range(n_qubits//2,n_qubits)), f"p{layer}"), list(range(n_qubits)), inplace=True)

            n_qubits = n_qubits//2

        self.circuit.compose(self.feature_map, self.all_qubits, inplace=True) # inplace to replace ?
        self.circuit.compose(self.instruction_set, self.all_qubits, inplace=True)


    def conv_layer(self, num_qubits, param_prefix):
        def conv_circuit(params):
            target = QuantumCircuit(2)
            target.rz(-np.pi / 2, 1)
            target.cx(1, 0)
            target.rz(params[0], 0)
            target.ry(params[1], 1)
            target.cx(0, 1)
            target.ry(params[2], 1)
            target.cx(1, 0)
            target.rz(np.pi / 2, 0)
            return target

        qc = QuantumCircuit(num_qubits, name="Convolutional Layer")
        qubits = list(range(num_qubits))
        param_index = 0
        params = ParameterVector(param_prefix, length=num_qubits * 3)
        for q1, q2 in zip(qubits[0::2], qubits[1::2]):
            qc = qc.compose(conv_circuit(params[param_index : (param_index + 3)]), [q1, q2])
            qc.barrier()
            param_index += 3
        for q1, q2 in zip(qubits[1::2], qubits[2::2] + [0]):
            qc = qc.compose(conv_circuit(params[param_index : (param_index + 3)]), [q1, q2])
            qc.barrier()
            param_index += 3

        qc_inst = qc.to_instruction()

        qc = QuantumCircuit(num_qubits)
        qc.append(qc_inst, qubits)
        return qc

    def pool_layer(self, sources, sinks, param_prefix):
        def pool_circuit(params):
            target = QuantumCircuit(2)
            target.rz(-np.pi / 2, 1)
            target.cx(1, 0)
            target.rz(params[0], 0)
            target.ry(params[1], 1)
            target.cx(0, 1)
            target.ry(params[2], 1)
            return target

        num_qubits = len(sources) + len(sinks)
        qc = QuantumCircuit(num_qubits, name="Pooling Layer")
        param_index = 0
        params = ParameterVector(param_prefix, length=num_qubits // 2 * 3)
        for source, sink in zip(sources, sinks):
            qc = qc.compose(pool_circuit(params[param_index : (param_index + 3)]), [source, sink])
            qc.barrier()
            param_index += 3

        qc_inst = qc.to_instruction()

        qc = QuantumCircuit(num_qubits)
        qc.append(qc_inst, range(num_qubits))
        return qc

        