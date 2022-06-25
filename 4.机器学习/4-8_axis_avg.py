import numpy as np
from random import randint

X = np.array([
    [randint(1,10) for x in range (4)]
    for y in range (4)
])

avg, var, std = np.average(X, axis=1), np.var(X, axis=1), np.std(X, axis=1)

print("Average: " + str(avg))
print("Variance: ", str(var))
print("Standard Deviations: " + str(std))