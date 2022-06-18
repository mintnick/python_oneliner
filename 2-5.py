# 寻找特定关键词，返回前后各18个字符

text = '''
Vue is a JavaScript framework for building user interfaces.
It builds on top of standard HTML, CSS and JavaScript, and provides
a declarative and component-based programming model that helps you
efficiently develop user interfaces, be it simple or complex.
'''

find = lambda x, q : x[x.find(q)-18 : x.find(q)+18] if q in x else -1

print(find(text, 'programming'))