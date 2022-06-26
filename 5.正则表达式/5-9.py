# find two same words that have less than 10 words between
import re

text = '''
A new and rapidly shifting reality took hold across America on Saturday as abortion, a basic legal right for nearly a half century, was outlawed in some states, and the initial bursts of elation and shock from the overturning of Roe v. Wade gave way to action.

At abortion clinics across the country, providers hastily canceled appointments out of fear of prosecution, and stunned women abruptly made plans to cross state lines into places where abortion was still allowed — traveling from Missouri to Illinois, from Wisconsin to Minnesota.

In Arkansas, where a trigger Arkansas law trigger banning abortions went into effect on Friday, 17 patients had been scheduled for abortions on Friday at Little Rock Family Planning Services, but none were performed before the Supreme Court’s decision shut down operations. About 30 more patients had been scheduled for an ultrasound and consultation that was required under Arkansas’ previous law before women could get an abortion.
'''

style_problem = re.search('\s(?P<x>[a-z]+)\s+([a-z]+\s+){0,10}(?P=x)\s', ' ' + text + ' ')

print(style_problem)