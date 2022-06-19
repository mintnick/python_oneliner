# multi dimension array slice

import numpy as np

a = np.array([
    [x for x in range (i, i+4)]
    for i in range (0, 13, 4)
])

print(a[:, 2])

print(a[1, :])

print(a[1, ::2])

print(a[:, :-1])

print(a[:-2])