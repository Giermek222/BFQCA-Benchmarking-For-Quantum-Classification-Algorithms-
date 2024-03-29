from cowskit.datasets.dataset import Dataset
from cowskit.files import DIABETES_DATASET
import numpy as np

class DiabetesDataset(Dataset):
    def __init__(self):
        Dataset.__init__(self)

    def generate_dataset(self):
        with open(DIABETES_DATASET, 'r') as file:
            diabetes_array = file.readlines()
            
            input_shape = (len(diabetes_array), 8)
            output_shape = (len(diabetes_array), 1)

            self.data = np.zeros(shape=input_shape, dtype=np.float64)
            self.labels = np.zeros(shape=output_shape, dtype=np.float64)

            for idx, entry in enumerate(diabetes_array):
                values = entry.replace('\n','').split(',')
                data = np.array([float(v) for v in values[:-1]])
                label = int(values[-1])

                self.data[idx,:] = data
                self.labels[idx, :] = 1 if label == 1 else -1

            divisor = np.amax(self.data, axis = 1)
            self.data = self.data / divisor[:, np.newaxis]