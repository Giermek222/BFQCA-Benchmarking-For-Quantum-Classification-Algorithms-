from typing import List
from cowskit.datasets.dataset import Dataset
from cowskit.constants import SHAPE_0D, SHAPE_1D, SHAPE_2D, SHAPE_3D
import numpy as np

class LinesDataset(Dataset):
    def __init__(self, ):
        Dataset.__init__(self, test_split = 0.1)

    def generate_dataset(self):
        amount = 10
        line_len = 3
        input_shape =  [amount, 4, 2]
        output_shape = [amount]

        assert(len(input_shape) in [SHAPE_2D, SHAPE_3D])
        assert(len(output_shape) in [SHAPE_0D, SHAPE_1D])
        if len(output_shape) == SHAPE_1D:
            assert(output_shape[1] == 1 or output_shape[1] == 2)

        labels_type = 0
        MULTI_CLASS = 1
        SINGLE_CLASS = 2
        CONSTANTS = 3
        
        self.data = np.random.rand(*input_shape)
        if len(output_shape) == SHAPE_1D and output_shape[1] != 1:
            self.labels = np.eye(output_shape[1])[np.random.choice(output_shape[1], amount)]
            labels_type = MULTI_CLASS
        elif len(output_shape) == SHAPE_1D and output_shape[1] == 1:
            self.labels = np.random.randint(2, size=(amount))
            self.labels = self.labels.reshape((amount,1))
            labels_type = SINGLE_CLASS
        else:
            self.labels = np.random.randint(2, size=(amount))
            labels_type = CONSTANTS


        for idx, label in enumerate(self.labels):
            if (labels_type == MULTI_CLASS and label[0] == 1) or \
                    (labels_type == SINGLE_CLASS and label[0] == 1) or \
                        (labels_type == CONSTANTS and label == 1):
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

        if len(self.labels.shape) == SHAPE_0D:
            self.labels = self.labels.reshape((amount, 1))

        if len(self.data.shape) == SHAPE_2D:
            self.data = self.data.reshape((amount, input_shape[1]*input_shape[2]))
        elif len(self.data.shape) == SHAPE_3D:
            self.data = self.data.reshape((amount, input_shape[1]*input_shape[2]*input_shape[3]))

