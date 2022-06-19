# max, min, average

import numpy as np
from random import randint

a = np.array([
    [randint(0,2) for x in range (3)]
    for y in range (3)
])

print(np.max(a))

print(np.min(a))

print(np.average(a))