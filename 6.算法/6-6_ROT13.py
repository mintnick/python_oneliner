abc = 'abcdefghijklmnopqrstuvwxyz'
s = 'xthexrussiansxarexcoming'

rt13 = lambda x: "".join(abc[(abc.find(c) + 13) % 26] for c in x)

print(rt13(s))
print(rt13(rt13(s)))