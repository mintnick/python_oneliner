# replace Sunday's data with average

import numpy as np
from random import randint

# temperature (Mon, Tue ...)
temp = np.array([
    randint(1,6) for x in range (7*3)
])
print(temp)

temp[6::7] = np.average(temp.reshape((-1, 7)), axis=1)

print(temp)