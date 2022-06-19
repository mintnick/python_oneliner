# array shape

import numpy as np
from random import randint

a = np.array([x for x in (1, 5)])
print(a)
print(a.shape)

b = np.array([
    [randint(1, 4) for x in range (3)]
    for y in range (3)
])
print(b)
print(b.shape)

c = np.array([
    [[randint(1,4) for x in range (3)]
    for y in range (3)]
    for z in range (2)
])
print(c)
print(c.shape)