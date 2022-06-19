# 打开一个文件，把每一行加入列表

filename = '2-3.py'

lines = [line.strip() for line in open(filename)]

print(lines)