# 修复损坏数据
import random

broswer = ['Firefox', 'Chrome', 'Safari']

visitors = [random.choice(broswer) for x in range (6)]

for i in range (len(visitors), 0, -1):
    visitors.insert(i, 'corrupted')

print(visitors)

visitors[1::2] = visitors[::2]

print(visitors)