# find the percentage of customer who bought both of books
import numpy as np
from random import randint

# [item1, item2, book1, book2]
basket = np.array([
    [randint(0, 1) for x in range (4)]
    for y in range (8)
])

copurchase = np.sum(np.all(basket[:, 2:], axis=1)) / basket.shape[0]

print(basket)
print(copurchase)