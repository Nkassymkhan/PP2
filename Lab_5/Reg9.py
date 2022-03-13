import re

s = input()

pattern = r'[A-Z][a-z]*'
n = re.findall(pattern, s)
print(' '.join((n)))