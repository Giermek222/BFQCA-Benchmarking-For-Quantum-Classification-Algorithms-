from cowskit.datasets.dataset import Dataset
from cowskit.files import PENGUINS_DATASET
import numpy as np

class PalmerPenguinDataset(Dataset):
    def __init__(self):
        Dataset.__init__(self)

    def generate_dataset(self):
        with open(PENGUINS_DATASET, 'r') as file:
            penguins_array = file.readlines()

            input_shape = (len(penguins_array), 6)
            output_shape = (len(penguins_array), 3)

            self.data = np.zeros(shape=input_shape, dtype=np.float64)
            self.labels = np.zeros(shape=output_shape, dtype=np.float64)

            for idx, entry in enumerate(penguins_array):
                values = entry.replace('\n','').split(',')
                data = np.array([float(v) for v in values[3:]])
                label = values[1]

                self.data[idx,:] = data
                if(label == "Adelie"):
                    self.labels[idx,:] = np.array([1,0,0])
                elif(label == "Gentoo"):
                    self.labels[idx,:] = np.array([0,1,0])
                elif(label == "Chinstrap"):
                    self.labels[idx,:] = np.array([0,0,1])
                else:
                    raise Exception(f"Unknown label in Palmer Penguins dataset: '{label}'")

            divisor = np.amax(self.data, axis = 1)
            self.data = self.data / divisor[:, np.newaxis]