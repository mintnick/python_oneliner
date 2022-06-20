import numpy as np
from random import randint

sat_scores = np.array([randint(1100, 1600) for x in range (7)])
students = np.array(['John', 'Bob', 'Alice', 'Joe', 'Jane', 'Frank', 'Carl'])

top_3 = students[np.argsort(sat_scores)][:-4:-1]

print(top_3)