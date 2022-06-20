# numpy 2d array slice

import numpy as np
from random import randint

inst = np.array([
    [232, '@instagram'],
    [133, '@selenagomex'],
    [59, '@victoriassecret'],
    [120, '@cristiano'],
    [76, '@nike']
])

superstars = inst[inst[:, 0].astype(float) > 100, 1]

print(superstars)