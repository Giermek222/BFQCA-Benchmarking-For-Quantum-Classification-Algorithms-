import numpy as np
import struct

from cowskit.datasets import IrisDataset, LinesDataset, PalmerPenguinDataset, DiabetesDataset
from cowskit.utils import bin_to_floatV2, float_to_binV2

t = "11111111101010000110001101110101"
n = bin_to_floatV2(t)
b = float_to_binV2(n)
print(t)
print(n)
print(b)

LinesDataset()
