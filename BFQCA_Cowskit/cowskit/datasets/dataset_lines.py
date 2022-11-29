from typing import List
from cowskit.datasets.dataset import Dataset
from cowskit.constants import SHAPE_2D, SHAPE_3D
import numpy as np

class LinesDataset(Dataset):
    def __init__(self, shape: List[int], line_len: int, validation_split: float = 0.1, test_split: float = 0.1, shuffle: bool = True):
        self.line_len = line_len

        input_shape = shape
        output_shape = (shape[0])
        assert(len(self.input_shape) in [SHAPE_2D, SHAPE_3D])

        Dataset.__init__(self, input_shape = input_shape, output_shape = output_shape, validation_split = validation_split, test_split = test_split, shuffle = shuffle)

    def generate_dataset(self):
        self.data = np.random.rand(*self.input_shape)
        self.labels = np.random.randint(low=0, high=2, size=self.output_shape)
        
        for idx, label in enumerate(self.labels):
            if label == 1:
                points_dims = self.input_shape[1:3]
                start_spot = [np.random.randint(low=0, high=dim) for dim in points_dims]
                direction = np.random.randint(low=0, high=4)

                if direction == 0:
                    end_spot = [max(start_spot[0] - self.line_len, 0), start_spot[1]]
                elif direction == 1:
                    end_spot = [min(start_spot[0] + self.line_len, points_dims[0] - 1), start_spot[1]]
                elif direction == 2:
                    end_spot = [start_spot[0], max(start_spot[1] - self.line_len, 0)]
                else:
                    end_spot = [start_spot[0], min(start_spot[1] + self.line_len, points_dims[1] - 1)]                

                if len(self.shape) == 3:
                    self.data[idx, start_spot[0]:end_spot[0], start_spot[1]:end_spot[1]] = 1
                else:
                    self.data[idx, start_spot[0]:end_spot[0], start_spot[1]:end_spot[1],:] = 1

    def ok(self):
        super().ok()