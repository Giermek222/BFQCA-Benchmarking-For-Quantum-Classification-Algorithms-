import numpy as np

a = np.ones((5,5))
a = np.pad(a, (0,2), 'constant', constant_values=(0))
print(a)