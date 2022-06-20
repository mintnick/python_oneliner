# nonzero function

import numpy as np
from random import randint
from random import uniform

X = np.array([
    [randint(20, 50) for x in range (5)]
    for y in range (4)
])

cities = np.array(['Hong Kong', 'New York', 'Berlin', 'Montreal'])

polluted = set(cities[np.nonzero(X > np.average(X))[0]])

print(X)
print(polluted)

# 3-4 with bool op
alice = [randint(90, 110) for x in range (3)]
bob = [randint(100, 120) for x in range (3)]
tim = [randint(85, 95) for x in range (3)]

people = np.array(['alice', 'bob', 'tim'])

salary = np.array([alice, bob, tim])
taxarion = np.array([
    [round(uniform(0.1, 0.5), 1) for x in range (3)]
    for y in range (3)
])

highest_staff = set(people[np.nonzero(salary*taxarion == np.max(salary*taxarion))[0]])

print(highest_staff)