from cowskit.datasets.dataset import Dataset
from typing import List

class Encoding:
    def __init__(self, dataset: Dataset = None):
        self.input_shape = dataset.output_shape
        self.output_shape:int = None

    def encode(self, value):
        return value
