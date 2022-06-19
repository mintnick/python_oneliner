# array type

import numpy as np

a = np.array([x for x in range(1, 5)], dtype=np.int16)
print(a)
print(a.dtype)

b = np.array([x for x in range(1, 5)], dtype=np.float64)
print(b)
print(b.dtype)