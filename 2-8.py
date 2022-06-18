# 清理第一个和最后两个数据，再复制多次创建新列表

import random
import matplotlib.pyplot as plt

caridc_cycle = [random.randint(60, 80) for x in range (10)]

expected_cycles = caridc_cycle[1:-2] * 10

plt.plot(expected_cycles)
plt.show()