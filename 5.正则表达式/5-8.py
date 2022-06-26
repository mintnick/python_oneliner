import re

text = '''
A new and rapidly shifting reality took hold across America on Saturday as abortion, a basic legal right for nearly a half century, was outlawed in some states, and the initial bursts of elation and shock from the overturning of Roe v. Wade gave way to action.

At abortion clinics across the country, providers hastily canceled appointments out of fear of prosecution, and stunned women abruptly made plans to cross state lines into places where abortion was still allowed — traveling from Missouri to Illinois, from Wisconsin to Minnesota.
'''

duplicates = re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)

print(duplicates)