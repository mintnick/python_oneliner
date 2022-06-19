# array math

import numpy as np
from random import randint

a = np.array([
    [randint(0,2) for x in range(3)]
    for y in range (3)
])

b = np.array([
    [randint(1,2) for x in range(3)]
    for y in range (3)
])

print(a)
print(b)

print(a+b)
print(a-b)
print(a*b)
print(a/b)