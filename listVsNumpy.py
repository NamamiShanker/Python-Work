import numpy as np
import time
arr = np.arange(10000)
current = time.time()
for i in arr:
    pass
print((time.time()-current)*1000)
current = time.time()
for i in np.nditer(arr):
    pass
print((time.time()-current)*1000)
