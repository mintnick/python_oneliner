# calculate income after tax

import numpy as np
from random import randint
from random import uniform

alice = [randint(90, 110) for x in range (3)]
bob = [randint(100, 120) for x in range (3)]
tim = [randint(85, 95) for x in range (3)]

salary = np.array([alice, bob, tim])
taxarion = np.array([
    [round(uniform(0.1, 0.5), 1) for x in range (3)]
    for y in range (3)
])

max_income = np.max(salary - salary * taxarion)

print(max_income)