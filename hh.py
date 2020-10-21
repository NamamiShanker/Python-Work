import numpy as np
arr = np.array([for i in range(100000)], dtype='int16')
for i in np.nditer(arr):
    print(i)
