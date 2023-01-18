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

class ConvolutionalModelV2(Model):
    def __init__(self) -> None:
        self.build_circuit()
        
    def train(self, X: np.ndarray, Y: np.ndarray) -> None:
        self.classifier.fit(X, Y)

    def predict(self, value: np.ndarray):
        return self.classifier.predict(value)
            
    def build_circuit(self):
        self.feature_map = ZFeatureMap(8)

        self.instruction_set = QuantumCircuit(8)

        self.instruction_set.compose(self.conv_layer(8), list(range(8)), inplace=True)
        self.instruction_set.compose(self.pool_layer(list(range(0,4)), list(range(4,8))), list(range(8)), inplace=True)

        self.instruction_set.compose(self.conv_layer(4), list(range(4, 8)), inplace=True)
        self.instruction_set.compose(self.pool_layer(list(range(0,2)), list(range(2,4))), list(range(4,8)), inplace=True)

        self.instruction_set.compose(self.conv_layer(2), list(range(6,8)), inplace=True)
        self.instruction_set.compose(self.pool_layer(list(range(0,1)), list(range(1,2))), list(range(6,8)), inplace=True)

        self.circuit = QuantumCircuit(8)
        self.circuit.compose(self.feature_map, range(8), inplace=True)
        self.circuit.compose(self.feature_map, range(8), inplace=True) # inplace to replace ?
        self.circuit.compose(self.instruction_set, range(8), inplace=True)

        observable = SparsePauliOp.from_list([("Z" + "I" * 7, 1)])

        self.network = EstimatorQNN(
            circuit=self.circuit.decompose(),
            input_params=self.feature_map.parameters,
            weight_params=self.instruction_set.parameters,
            observables=observable
        )

        # def callback_graph(weights, obj_func_eval):
        #     clear_output(wait=True)
        #     objective_func_vals.append(obj_func_eval)
        #     plt.title("Objective function value against iteration")
        #     plt.xlabel("Iteration")
        #     plt.ylabel("Objective function value")
        #     plt.plot(range(len(objective_func_vals)), objective_func_vals)
        #     plt.show()

        self.classifier = NeuralNetworkClassifier(
            self.network,
            optimizer=ADAM(maxiter=200),
            # callback=callback_graph
        )


    def conv_layer(self, num_qubits, param_prefix = "c"):
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
        params = ParameterVector(param_prefix + str(random.randint(0,10000)), length=num_qubits * 3)
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

    def pool_layer(self, sources, sinks, param_prefix = "p"):
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
        params = ParameterVector(param_prefix + str(random.randint(0,10000)), length=num_qubits // 2 * 3)
        for source, sink in zip(sources, sinks):
            qc = qc.compose(pool_circuit(params[param_index : (param_index + 3)]), [source, sink])
            qc.barrier()
            param_index += 3

        qc_inst = qc.to_instruction()

        qc = QuantumCircuit(num_qubits)
        qc.append(qc_inst, range(num_qubits))
        return qc

        