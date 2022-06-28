from functools import reduce

n = 10

fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])

print(fibs)

x = [0, 1]
fibs = x[0:2] + [x.append(x[-1] + x[-2]) or x[-1] for i in range(n-2)]
# append doesn't return the value, use OR operation to get the appended element
print(fibs)
