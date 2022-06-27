from functools import reduce

s = {1, 2, 3}

ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])

print(ps(s))

for x in s:
    print(x)