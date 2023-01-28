from typing import List
from cowskit.datasets.dataset import Dataset
from cowskit.constants import SHAPE_0D, SHAPE_1D, SHAPE_2D, SHAPE_3D
import numpy as np

class NoisyDataset(Dataset):
    def __init__(self, amount = 100, i_dim = 4, o_dim = 2):
        self.amount = int(amount)
        self.input_dim = int(i_dim)
        self.output_dim = int(o_dim)
        Dataset.__init__(self)

    def generate_dataset(self):
        self.data = np.random.rand(self.amount, self.input_dim)

        if self.output_dim != 1:
            self.labels = np.eye(self.output_dim)[np.random.choice(self.output_dim, self.amount)]
        else:
            self.labels = np.random.randint(2, size=(self.amount))
            self.labels = (self.labels * 2) - 1
            self.labels = self.labels.reshape((self.amount,1))