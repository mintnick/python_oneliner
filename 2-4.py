# 标记包含字符串的元素

text = [
    'Nearly all Markdown applications support the basic syntax outlined in the',
    'original Markdown design document. There are minor variations and discrepancies',
    'between Markdown processors — those are noted inline wherever possible.'
]

mark = map(lambda s : (True, s) if 'Markdown' in s else (False, s), text)

print(list(mark))

# 练习：使用列表解析
mark = [[(True, line) if 'Markdown' in line else (False, line)] for line in text]

print(mark)