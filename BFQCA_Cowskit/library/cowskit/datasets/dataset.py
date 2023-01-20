from typing import Tuple
import numpy as np
from random import randint
from cowskit.constants import SHAPE_0D, SHAPE_1D

class Dataset:

    def __init__(self, test_split: float = 0.1, limit: int = 10):
        """
        This function must be called when creating a custom instance of a dataset class.\n
        Dataset.__init__(self) or Dataset.__init__(self, test_split)\n
        test_split default value: 0.1
        """
        self.test_split = test_split
        self.limit = limit # 0 or less - no limit
        
        self.data:np.ndarray = None
        self.labels:np.ndarray = None
        self._validated = False

        self.generate_dataset()
        self.validate()
        self.cut()

        self.X_train, self.X_test, self.y_train, self.y_test = self.train_test_split()

    def generate_dataset(self) -> None:
        """
        Override this method. \n
        Set the following class parameters to numpy arrays:\n
        self.data, self.labels.
        """
        raise Exception("Unimplemented 'generate_dataset' function in custom dataset.")

    def shuffle(self) -> None:
        assert(self._validated == True)
        indices = np.arange(0, self.len)
        np.random.shuffle(indices)

        self.data = self.data[indices]
        self.labels = self.labels[indices]

    def train_test_split(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        assert(self._validated == True)
        self.shuffle()
        divisor_idx = int(self.len * self.test_split)
        if divisor_idx == self.len:
            divisor_idx -= 1
        test_indices = np.arange(0, divisor_idx)
        train_indices = np.arange(divisor_idx, self.len)

        self.train_len = len(train_indices)
        self.test_split = len(test_indices)

        return self.data[train_indices], self.data[test_indices], self.labels[train_indices], self.labels[test_indices]

    def get_train_data(self) -> Tuple[np.ndarray, np.ndarray]:
        assert(self._validated == True)
        return self.X_train, self.y_train

    def get_test_data(self) -> Tuple[np.ndarray, np.ndarray]:
        assert(self._validated == True)
        return self.X_test, self.y_test

    def get_random_pair(self) -> Tuple[np.ndarray, np.ndarray]:
        assert(self._validated == True)
        idx = randint(0, self.len - 1)
        x = np.expand_dims(self.data[idx], axis=0)
        y = np.expand_dims(self.labels[idx], axis=0)
        return x,y

    def validate(self):
        assert(self.data is not None)
        assert(self.labels is not None)
        assert(self.data.shape[0] == self.labels.shape[0])
        assert(self.test_split > 0 and self.test_split < 1)
        assert(len(self.data.shape) == SHAPE_1D)
        assert(len(self.labels.shape) == SHAPE_1D)

        self.input_size = self.data.shape[1]
        self.output_size = self.data.shape[1]
        self._validated = True

    def cut(self):
        if self.limit >= 0 and self.limit < self.data.shape[0]:
            self.data = self.data[:self.limit, :]
            self.labels = self.labels[:self.limit, :]
        self.len = self.data.shape[0]


