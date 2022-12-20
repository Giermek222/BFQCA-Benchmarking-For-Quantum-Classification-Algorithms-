from cowskit.encodings.encoding import Encoding
from cowskit.datasets.dataset import Dataset

class BinaryEncoding(Encoding):
    def __init__(self, dataset: Dataset = None):
        Encoding.__init__(self, dataset)