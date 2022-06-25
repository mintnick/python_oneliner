import re

report = '''
Grants of $37 billion were $4.2 billion higher compared with 2019-20.
The increase was largely driven by an increase in GST revenue of $2.7 billion
resulting from a sharp recovery in consumption and dwelling investment, despite Victoria's 
assessed GST relativity falling again in 2020-21. There was also a year-on-year increase 
in various specific purpose grants.
'''

dollors = [x[0] for x in re.findall('(\$[0-9]+(\.[0-9]*)?)', report)]

print(dollors)