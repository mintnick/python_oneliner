# 截取样本
import random

data = [[round(random.uniform(1.1, 9.9), 1) for x in range(6)] for x in range(4)]

sample = [line[::2] for line in data]

print(sample)