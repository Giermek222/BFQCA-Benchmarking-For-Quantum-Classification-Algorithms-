from typing import List
from cowskit.datasets.dataset import Dataset
from cowskit.constants import SHAPE_0D, SHAPE_1D, SHAPE_2D, SHAPE_3D
import numpy as np

class LinesDataset(Dataset):
    def __init__(self, ):
        Dataset.__init__(self)

    def generate_dataset(self):
        amount = 20
        input_shape =  [amount, 2, 2]
        output_shape = [amount, 1]
        line_len = input_shape[1]

        assert(len(input_shape) in [SHAPE_2D, SHAPE_3D])
        assert(len(output_shape) in [SHAPE_1D])
        assert(output_shape[1] == 1 or output_shape[1] == 2)

        self.data = np.random.rand(*input_shape)
        if output_shape[1] != 1:
            self.labels = np.eye(output_shape[1])[np.random.choice(output_shape[1], amount)]
        else:
            self.labels = np.random.randint(2, size=(amount))
            self.labels = self.labels.reshape((amount,1))

        for idx, label in enumerate(self.labels):
            if label[0] == 1:
                image_shape = input_shape[1:]
                start_spot_coords = [np.random.randint(low=0, high=dim) for dim in image_shape]
                direction = np.random.randint(low=0, high=4)

                if direction == 0: # left
                    src = start_spot_coords[0]
                    dst = max(start_spot_coords[0] - line_len, 0)
                    src, dst = (src, dst) if src <= dst else (dst, src)
                    start_spot_coords = [src, start_spot_coords[1]]
                    end_spot_coords = [dst, start_spot_coords[1]]
                elif direction == 1: # right
                    src = start_spot_coords[0]
                    dst = min(start_spot_coords[0] + line_len, image_shape[0] - 1)
                    src, dst = (src, dst) if src <= dst else (dst, src)
                    start_spot_coords = [src, start_spot_coords[1]]
                    end_spot_coords = [dst, start_spot_coords[1]]
                elif direction == 2: # up
                    src = start_spot_coords[1]
                    dst = max(start_spot_coords[1] - line_len, 0)
                    src, dst = (src, dst) if src <= dst else (dst, src)
                    start_spot_coords = [start_spot_coords[0], src]
                    end_spot_coords = [start_spot_coords[0], dst]
                else: # down
                    src = start_spot_coords[1]
                    dst = min(start_spot_coords[1] + line_len, image_shape[1] - 1)
                    src, dst = (src, dst) if src <= dst else (dst, src)
                    start_spot_coords = [start_spot_coords[0], src]
                    end_spot_coords = [start_spot_coords[0], dst]

                block_of_data = self.data[idx, start_spot_coords[0]:end_spot_coords[0] + 1, start_spot_coords[1]:end_spot_coords[1] + 1]
                if isinstance(block_of_data, np.ndarray):
                    self.data[idx, start_spot_coords[0]:end_spot_coords[0] + 1, start_spot_coords[1]:end_spot_coords[1] + 1] = np.ones(block_of_data.shape)
                else:
                    self.data[idx, start_spot_coords[0]:end_spot_coords[0] + 1, start_spot_coords[1]:end_spot_coords[1] + 1] = 1

        if len(self.data.shape) == SHAPE_2D:
            self.data = self.data.reshape((amount, input_shape[1]*input_shape[2]))
        elif len(self.data.shape) == SHAPE_3D:
            self.data = self.data.reshape((amount, input_shape[1]*input_shape[2]*input_shape[3]))

