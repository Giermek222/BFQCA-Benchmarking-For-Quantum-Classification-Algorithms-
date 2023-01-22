import math
import numpy as np
from typing import Tuple
from random import randint

from cowskit.constants import SHAPE_1D, MAX_QUBITS
from cowskit.utils import get_shape_size

class Dataset:

    def __init__(self, test_split: float = 0.3, limit: int = 20):
        """
        This function must be called when creating a custom instance of a dataset class.\n
        Dataset.__init__(self) or Dataset.__init__(self, test_split)\n
        test_split default value: 0.1
        """
        self.test_split = test_split
        self.limit = limit # 0 or less - no limit
        
        self.data:np.ndarray = None
        self.labels:np.ndarray = None
        self.X_train:np.ndarray = None 
        self.X_test:np.ndarray = None
        self.y_train:np.ndarray = None
        self.y_test:np.ndarray = None

        self.input_size:int = None
        self.output_size:int = None
        self.input_padding_amount:int = None
        self.output_padding_amount:int = None

        self._validated = False
        self.generate_dataset()
        self.pad_and_validate()
        self.train_test_split()

    def generate_dataset(self) -> None:
        """
        Override this method. \n
        Set the following class parameters to numpy arrays:\n
        self.data, self.labels.
        """
        raise Exception("Unimplemented 'generate_dataset' function in custom dataset.")

    # ======================== INTERNAL FUNCTIONS ========================
    def get_input_size(self) -> int:
        return self.input_size + self.input_padding_amount

    def get_output_size(self) -> int:
        return self.output_size + self.output_padding_amount

    def get_random_pair(self) -> Tuple[np.ndarray, np.ndarray]:
        assert(self._validated == True)
        idx = randint(0, self.len - 1)
        x = np.expand_dims(self.data[idx], axis=0)
        y = np.expand_dims(self.labels[idx], axis=0)
        return x,y

    def pad_and_validate(self):
        assert(self.data is not None)
        assert(self.labels is not None)
        assert(self.data.shape[0] == self.labels.shape[0])
        assert(self.test_split > 0 and self.test_split < 1)
        assert(len(self.data.shape) == SHAPE_1D)
        assert(len(self.labels.shape) == SHAPE_1D)

        self.input_size = self.data.shape[1]
        self.output_size = self.labels.shape[1]

        self.add_quantum_padding()

        self.input_padding_amount = self.data.shape[1] - self.input_size
        self.output_padding_amount = self.labels.shape[1] - self.output_size

        assert(self.get_input_size() <= MAX_QUBITS)
        assert(self.get_output_size() <= MAX_QUBITS)

        self.len = self.data.shape[0]
        self._validated = True

    def add_quantum_padding(self) -> None:
        data_pad_amount = get_shape_size(self.data)
        data_nearest_pow_of_two = int(math.pow(2, math.ceil(math.log2(data_pad_amount))))
        data_pad_amount = data_nearest_pow_of_two - data_pad_amount

        if data_pad_amount != 0:
            data_padding = np.zeros((self.data.shape[0], data_pad_amount))
            self.data = np.concatenate((self.data, data_padding), axis = 1)

        labels_pad_amount = get_shape_size(self.labels)
        labels_nearest_pow_of_two = int(math.pow(2, math.ceil(math.log2(labels_pad_amount))))
        labels_pad_amount = labels_nearest_pow_of_two - labels_pad_amount

        if labels_pad_amount != 0:
            labels_padding = np.zeros((self.labels.shape[0], labels_pad_amount))
            self.labels = np.concatenate((self.labels, labels_padding), axis = 1)

    def shuffle(self) -> None:
        indices = np.arange(0, self.data.shape[0])
        np.random.shuffle(indices)

        self.data = self.data[indices]
        self.labels = self.labels[indices]

    def cut(self):
        if self.limit >= 0 and self.limit < self.data.shape[0]:
            self.data = self.data[:self.limit, :]
            self.labels = self.labels[:self.limit, :]
        self.len = self.data.shape[0]

    def train_test_split(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        assert(self._validated == True)
        self.shuffle()
        self.cut()

        divisor_idx = int(self.data.shape[0] * self.test_split)
        if divisor_idx == self.data.shape[0]:
            divisor_idx -= 1
        test_indices = np.arange(0, divisor_idx)
        train_indices = np.arange(divisor_idx, self.data.shape[0])

        self.train_len = len(train_indices)
        self.test_split = len(test_indices)

        self.X_train, self.X_test = self.data[train_indices], self.data[test_indices]
        self.y_train, self.y_test = self.labels[train_indices], self.labels[test_indices]

        return self.X_train, self.X_test, self.y_train, self.y_test

    def get_train_data(self) -> Tuple[np.ndarray, np.ndarray]:
        assert(self._validated == True)
        return self.X_train, self.y_train

    def get_test_data(self) -> Tuple[np.ndarray, np.ndarray]:
        assert(self._validated == True)
        return self.X_test, self.y_test





