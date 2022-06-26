# replace, with ?!
import re

text = '''
A new and rapidly shifting reality took hold across America on Saturday as abortion
'''

updated = re.sub("abortion(?!')", 'ABORTION', text) # not end with '

print(updated)