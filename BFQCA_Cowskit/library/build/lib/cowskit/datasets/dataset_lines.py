from typing import List
from cowskit.datasets.dataset import Dataset
from cowskit.constants import SHAPE_2D, SHAPE_3D
import numpy as np

class LinesDataset(Dataset):
    def __init__(self, ):
        Dataset.__init__(self, test_split = 0.1)

    def generate_dataset(self):
        amount = 10
        line_len = 3
        input_shape =  (amount,4,2)
        output_shape = (amount,1) # 2 -> 1

        assert(len(input_shape) in [SHAPE_2D, SHAPE_3D])

        self.data = np.random.rand(*input_shape)
        # self.labels = np.eye(output_shape[1])[np.random.choice(output_shape[1], amount)]
        self.labels = np.random.randint(2, size=(amount))

        for idx, label in enumerate(self.labels):
            #if label[1] == 1:
            if label == 1:
                image_shape = input_shape[1:]
                start_spot_coords = [np.random.randint(low=0, high=dim) for dim in image_shape]
                direction = np.random.randint(low=0, high=4)

                if direction == 0:
                    end_spot_coords = [max(start_spot_coords[0] - line_len, 0), start_spot_coords[1]]
                elif direction == 1:
                    end_spot_coords = [min(start_spot_coords[0] + line_len, image_shape[0] - 1), start_spot_coords[1]]
                elif direction == 2:
                    end_spot_coords = [start_spot_coords[0], max(start_spot_coords[1] - line_len, 0)]
                else:
                    end_spot_coords = [start_spot_coords[0], min(start_spot_coords[1] + line_len, image_shape[1] - 1)]                

                block_of_data = self.data[idx, start_spot_coords[0]:end_spot_coords[0], start_spot_coords[1]:end_spot_coords[1]]
                if isinstance(block_of_data, np.ndarray):
                    self.data[idx, start_spot_coords[0]:end_spot_coords[0], start_spot_coords[1]:end_spot_coords[1]] = np.ones(block_of_data.shape)
                else:
                    self.data[idx, start_spot_coords[0]:end_spot_coords[0], start_spot_coords[1]:end_spot_coords[1]] = 1

        self.labels = self.labels.reshape((amount)) #
        self.data = self.data.reshape((amount, 8)) #
