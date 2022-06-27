factorial = lambda x: x * factorial(x-1) if x > 1 else 1

print(factorial(3))
print(factorial(4))
print(factorial(1))