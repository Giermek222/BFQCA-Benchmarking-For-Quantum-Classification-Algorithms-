import numpy as np


class Amplitude_Encoding():
    """
    class containing logic form encoding classical data to normalised quantum vectors.
    """

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
