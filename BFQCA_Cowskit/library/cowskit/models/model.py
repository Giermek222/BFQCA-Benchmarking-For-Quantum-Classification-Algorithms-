from cowskit.datasets.dataset import Dataset
from cowskit.algorithms.algorithm import Algorithm

class Model(Algorithm):
    def __init__(self, dataset: Dataset = None) -> None:
        Algorithm.__init__(self, dataset)
