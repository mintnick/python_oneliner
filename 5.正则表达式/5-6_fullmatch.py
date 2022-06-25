import re
from random import randint

inputs = [
    str(randint(1,99)) + ':' + str(randint(1,99))
    for x in range (6)
]

inputs.append("aa:bb")

input_ok = lambda x: re.fullmatch('[0-9]{2}:[0-9]{2}', x) != None

for x in inputs:
    print(input_ok(x))

print(inputs)