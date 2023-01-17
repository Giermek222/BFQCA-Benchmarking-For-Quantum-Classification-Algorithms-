from cowskit.datasets.dataset import Dataset
from cowskit.files import IRIS_DATASET
import numpy as np

import sklearn.datasets as skdatasets
from sklearn.model_selection import train_test_split

class IrisDataset(Dataset):
    def __init__(self, test_split: float = 0.1):
        Dataset.__init__(self, test_split = test_split)

    def generate_dataset(self):
        with open(IRIS_DATASET, 'r') as file:
            iris_array = file.readlines()
            input_shape = (len(iris_array), 4)
            output_shape = (len(iris_array), 3)

            self.data = np.zeros(shape=input_shape, dtype=np.float64)
            self.labels = np.zeros(shape=output_shape, dtype=np.float64)

            for idx, entry in enumerate(iris_array):
                values = entry.replace('\n','').split(',')
                data = np.array([float(v) for v in values[:-1]])
                label = values[-1]

                self.data[idx,:] = data
                if(label == "Iris-setosa"):
                    self.labels[idx,:] = np.array([1,0,0])
                elif(label == "Iris-versicolor"):
                    self.labels[idx,:] = np.array([0,1,0])
                elif(label == "Iris-virginica"):
                    self.labels[idx,:] = np.array([0,0,1])
                else:
                    raise Exception(f"Unknown label in Iris Dataset: '{label}'")

            divisor = np.amax(self.data)
            self.data /= divisor

    def load_iris(self, train_size:int, test_size:int):

        X, Y= skdatasets.load_iris(return_X_y=True)

        return train_test_split(
            X, Y, test_size=test_size, train_size=train_size, random_state=42
        )