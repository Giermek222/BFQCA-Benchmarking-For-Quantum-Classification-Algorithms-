import numpy as np
from qiskit import QuantumCircuit, QuantumRegister


class AmplitudeEncodingV2:
    """
    class containing logic form encoding classical data to normalised quantum vectors.
    """

    def __init__(self, n_features: int = 2):
        # in n qubits we can store 2^n features
        n_qubits = np.log2(n_features)
        if not n_qubits.is_integer():
            # if number of qubits is not a positive
            # power of 2, an extra qubit is needed
            n_qubits = np.ceil(n_qubits)
        elif n_qubits == 0:
            # in this scenario, n_features = 1
            # then we need 1 qubit
            n_qubits = 1

        self.num_qubits = int(n_qubits)
        self.num_features = n_features

    def _check_feature_vector(self, x):
        if len(x) != self.num_features:
            raise ValueError(f"Expected features dimension "
                             f"{self.num_features}, but {len(x)} was passed")

    def construct_circuit(self, x) -> QuantumCircuit:
        """
        :param x: data that we want to encode
        :return:
        """
        self._check_feature_vector(x)
        if self.num_features % 2 != 0:
            # if not power of 2, pad with zeros
            x = np.pad(x, (0, (1 << self.num_qubits) - len(x)))

        state_vector = self.encode(x)

        q = QuantumRegister(self.num_qubits)
        qc = QuantumCircuit(q)
        qc.initialize(state_vector, [q[i] for i in range(self.num_qubits)])

        qc.data = [d for d in qc.data if d[0].name != "reset"]
        return qc

    def encode(self, classical_data):
        """
        Args:
            classical_data as a numpy array
        Returns:
            return normalised vector of qubits
        """
        norm = np.linalg.norm(classical_data)
        if norm == 0:
            norm = 1
        # should I also round it 3/4 decimals?
        normalised_vector = classical_data / norm
        return normalised_vector