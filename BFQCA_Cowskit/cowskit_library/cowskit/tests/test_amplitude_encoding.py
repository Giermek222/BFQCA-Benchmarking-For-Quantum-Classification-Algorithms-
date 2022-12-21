import unittest
import numpy as np
from cowskit.encodings import AmplitudeEncoding

class MyTestCase(unittest.TestCase):
    encoding_map = AmplitudeEncoding()

    starting_data = [
        np.array([1, 1, 1, 1]),
        np.array([0, 0, 0, 0]),
        np.array([0.1, -0.7, 1, 0]),
    ]
    correct_encoded_data = [
        np.array([0.5, 0.5, 0.5, 0.5]),
        np.array([0, 0, 0, 0]),
        np.array([0.081, -0.571, 0.816, 0.]),
    ]

    def test_amplitude_encoding(self):
        encoded_data = [
            self.encoding_map.encode(data) for data in self.starting_data
        ]
        np.testing.assert_allclose(encoded_data, self.correct_encoded_data, rtol= 0.01, atol= 0.01)

if __name__ == '__main__':
    unittest.main()