# slice and assign

import numpy as np
from random import randint

dataScientist = [randint(130, 140) for x in range (3)]
productManager = [randint(125, 150) for x in range (3)]
designer = [randint(110,130) for x in range (3)]
softwareEngineer = [randint(130, 140) for x in range (3)]

employees = np.array([
    dataScientist,
    productManager,
    designer,
    softwareEngineer
])
print(employees)

# increase data scientist's salary every second year
employees[0, ::2] = employees[0, ::2] * 1.1

print(employees)