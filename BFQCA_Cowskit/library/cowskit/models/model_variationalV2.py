import qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import ZFeatureMap
from qiskit_machine_learning.algorithms.classifiers import NeuralNetworkClassifier
from qiskit_machine_learning.neural_networks import EstimatorQNN
from qiskit.algorithms.optimizers.adam_amsgrad import ADAM
from qiskit.quantum_info import SparsePauliOp
import random

import numpy as np

from cowskit.models.model import Model
from cowskit.datasets.dataset import Dataset
from cowskit.encodings.encoding import Encoding

class VariationalModelV2(Model):
    def __init__(self) -> None:
        Model.__init__(self)
        self.EPOCHS = 1
        
    def train(self, X: np.ndarray, Y: np.ndarray) -> None:
        self.build_circuit()
        Y = Y.flatten()
        self.classifier.fit(X, Y)

    def predict(self, value: np.ndarray):
        return self.classifier.predict(value)
            
    def build_circuit(self):
        self.feature_map = ZFeatureMap(8)
        self.instruction_set = QuantumCircuit(8)

        self.instruction_set.compose(self.dense_layer(8, 0), list(range(8)), inplace=True)
        self.instruction_set.compose(self.dense_layer(8, 1), list(range(8)), inplace=True)
        self.instruction_set.compose(self.dense_layer(8, 2), list(range(8)), inplace=True)
        self.instruction_set.compose(self.dense_layer(8, 3), list(range(8)), inplace=True)
        self.instruction_set.compose(self.dense_layer(8, 4), list(range(8)), inplace=True)
        self.instruction_set.compose(self.dense_layer(8, 5), list(range(8)), inplace=True)
        self.instruction_set.compose(self.dense_layer(8, 6), list(range(8)), inplace=True)
        self.instruction_set.compose(self.dense_layer(8, 7), list(range(8)), inplace=True)

        self.circuit = QuantumCircuit(8)
        self.circuit.compose(self.feature_map, range(8), inplace=True)
        self.circuit.compose(self.instruction_set, range(8), inplace=True)

        observable = SparsePauliOp.from_list([("Z" + "I" * 7, 1)])

        self.network = EstimatorQNN(
            circuit=self.circuit.decompose(),
            input_params=self.feature_map.parameters,
            weight_params=self.instruction_set.parameters,
            observables=observable
        )

        self.classifier = NeuralNetworkClassifier(
            self.network,
            optimizer=ADAM(maxiter=self.EPOCHS),
        )


    def dense_layer(self, num_qubits, id, param_prefix = "c"):
        def weights_circuit(params):
            target = QuantumCircuit(num_qubits)
            layer = 0
            for i in range(num_qubits):
                target.rx(params[3*i + 0], i)
                target.ry(params[3*i + 1], i)
                target.rz(params[3*i + 2], i)
                layer += 1
            return target

        def entanglement_circuit(offset):
            target = QuantumCircuit(num_qubits)
            for i in range(num_qubits):
                src = offset + i
                dst = offset + i + 1
                if src >= num_qubits:
                    src -= num_qubits
                if dst >= num_qubits:
                    dst -= num_qubits
                
                target.cx(dst, src)
            return target

        qc = QuantumCircuit(num_qubits, name="Dense Layer")
        qubits = list(range(num_qubits))
        params = ParameterVector(param_prefix + str(id), length=num_qubits * 3)

        
        qc = qc.compose(weights_circuit(params), qubits)
        qc = qc.compose(entanglement_circuit(id), qubits)
        qc.barrier()

        qc_inst = qc.to_instruction()

        qc = QuantumCircuit(num_qubits)
        qc.append(qc_inst, qubits)
        return qc