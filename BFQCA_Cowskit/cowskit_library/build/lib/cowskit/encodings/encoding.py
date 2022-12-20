from cowskit.datasets.dataset import Dataset
from cowskit.utils.decorators import *
from typing import List

class Encoding:
    def __init__(self, dataset: Dataset = None):
        self.input_shape = dataset.output_shape
        self.output_shape:int = None

    @VirtualHandle
    def encode(self, value):
        return value
