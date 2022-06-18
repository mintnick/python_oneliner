# 生成列表，每个元素也是一个列表，包含一行中所有多于3个字符的单词

text = '''
Nearly all Markdown applications support the basic syntax outlined in the 
original Markdown design document. There are minor variations and discrepancies 
between Markdown processors — those are noted inline wherever possible.
'''

w = [[x for x in line.split() if len(x) > 3] for line in text.split('\n')]

print(w)
