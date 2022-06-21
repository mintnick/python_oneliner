# find books higher than lowest

import numpy as np

books = np.array([
    ['A', 4.6],
    ['B', 5.0],
    ['C', 4.3],
    ['D', 3.9],
    ['E', 2.2],
    ['F', 4.7]
])

predict_bestseller = lambda x, y : x[x[:,1].astype(float) > y]

print(predict_bestseller(books, 3.9))