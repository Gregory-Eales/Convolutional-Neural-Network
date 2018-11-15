# import dependencies
import numpy as np
#from ConvNet import ConvNet
#import DataHandling



x = np.ones([2, 2])

x = np.pad(x, [(1, 1), (1, 1)], mode="constant")

print(x)
