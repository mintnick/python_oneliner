import numpy as np
from random import randint

# [item1, item2, book1, book2]
basket = np.array([
    [randint(0,1) for x in range (4)]
    for y in range (8)
])

copurchases = [(i,j,np.sum(basket[:,i] + basket[:,j] == 2))
            for i in range (4) for j in range (i+1, 4)]

print(basket)
print(max(copurchases, key=lambda x:x[2]))