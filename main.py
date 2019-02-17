# import dependencies
import numpy as np
from conv2 import Convolutional_Neural_Network
from DataHandling import get_data


x, y = get_data()

print(x.shape)

CNN = Convolutional_Neural_Network(x, y)

