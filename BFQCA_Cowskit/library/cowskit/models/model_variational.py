import qiskit
from qiskit import QuantumCircuit
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

class VariationalModel(Model):
    def __init__(self, dataset: Dataset) -> None:
        Model.__init__(self, dataset)
        self.EPOCHS = 1
        
    def train(self, X: np.ndarray, Y: np.ndarray) -> None:
        if self.get_output_size() == 1:
            Y = Y.flatten()

        self.build_circuit()
        self.classifier.fit(X, Y)

    def predict(self, value: np.ndarray):
        return self.classifier.predict(value)
            
    def build_circuit(self):
        in_size = self.get_input_size()
        out_size = self.get_output_size()

        self.feature_map = ZFeatureMap(in_size)
        self.instruction_set = QuantumCircuit(in_size)

        all_qubits = list(range(in_size))
        layer_id = 0
        while True:
            self.instruction_set.compose(self.dense_layer(in_size, layer_id), all_qubits, inplace=True)
            layer_id += 1

            if layer_id == in_size:
                break

        self.circuit = QuantumCircuit(in_size)
        self.circuit.compose(self.feature_map,     all_qubits, inplace=True)
        self.circuit.compose(self.instruction_set, all_qubits, inplace=True)


        observables = [0]*out_size
        for i in range(out_size):
            ignore_string = ["I"] * in_size
            ignore_string[i] = "Z"
            measure_single_z_string = "".join(ignore_string)
            observables[i] = SparsePauliOp.from_list([(measure_single_z_string, 1)])

        self.network = EstimatorQNN(
            circuit=self.circuit.decompose(),
            input_params=self.feature_map.parameters,
            weight_params=self.instruction_set.parameters,
            observables=observables
        )

        self.classifier = NeuralNetworkClassifier(
            self.network,
            one_hot=True if out_size != 1 else False,
            optimizer=ADAM(maxiter=self.EPOCHS),
        )


    def dense_layer(self, num_qubits, id):
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
        params = ParameterVector(f"dense_{str(id+1)}", length=num_qubits * 3)

        offset = id - 1
        qc = qc.compose(weights_circuit(params), qubits)
        qc = qc.compose(entanglement_circuit(offset), qubits)
        qc.barrier()

        qc_inst = qc.to_instruction()

        qc = QuantumCircuit(num_qubits)
        qc.append(qc_inst, qubits)
        return qc