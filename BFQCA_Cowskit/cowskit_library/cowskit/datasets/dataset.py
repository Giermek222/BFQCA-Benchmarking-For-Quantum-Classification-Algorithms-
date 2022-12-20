from typing import Tuple, List
import numpy as np
from cowskit.utils.decorators import *

class Dataset:

    def __init__(self, input_shape:List = None, output_shape:List = None, validation_split: float = 0.1, test_split: float = 0.1, shuffle: bool = True):
        self.validation_split = validation_split
        self.test_split = test_split
        self.shuffle = shuffle

        self.input_shape = input_shape
        self.output_shape = output_shape
        
        self.data:np.ndarray = None
        self.labels:np.ndarray = None

        
        self._validated = False

        self.generate_dataset()
        self.ok()

    def __len__(self) -> int:
        return self.data.shape[0]

    def __iter__(self):
        self._idx = 0
        return self.data[self._idx], self.labels[self._idx]

    def __next__(self) -> Tuple[np.ndarray, np.ndarray]:
        self._idx += 1
        if(self._idx == self.data.shape[0]):
            raise StopIteration
        return self.data[self._idx], self.labels[self._idx]

    def __call__(self) -> np.ndarray:
        if self.shuffle:
            indices = np.arange(0, self.data.shape[0])
            np.random.shuffle(indices)

            self.data = self.data[indices]
            self.labels = self.labels[indices]
        return self.data

    def __contains__(self, item) -> bool:
        return self.data.any(item, axis=0)

    def ok(self):
        assert(self.input_shape is not None)
        assert(self.output_shape is not None)
        assert(self.data is not None)
        assert(self.labels is not None)
        assert(self.data.shape == self.input_shape)
        assert(self.labels.shape == self.output_shape)

        self.validated = True

    @VirtualHandle
    def generate_dataset(self) -> None:
        None

    def get_example(self) -> np.ndarray:
        return self.data[0]