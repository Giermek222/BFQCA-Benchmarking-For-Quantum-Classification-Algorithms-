from cowskit.datasets.dataset import Dataset
from cowskit.files import IRIS_DATASET
import numpy as np

class IrisDataset(Dataset):
    def __init__(self):
        Dataset.__init__(self, test_split=0.5)

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

            divisor = np.amax(self.data, axis = 0)
            self.data = self.data / divisor[:]

