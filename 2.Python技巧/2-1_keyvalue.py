# 找出列表中收入至少10万者

employees = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121,
}

result = {(k, v) for k, v in employees.items() if v >= 100000}

print(result)