from random import randint

unsorted = [randint(1,30) for x in range(10)]

qs = lambda l: qs([x for x in l[1:] if x<= l[0]]) + [l[0]] + qs([x for x in l if x>l[0]]) if l else []

print(unsorted)
print(qs(unsorted))