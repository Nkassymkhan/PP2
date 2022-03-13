import re

s = input()

pattern = r'[A-Z][^A-Z]*'

print(re.findall(pattern, s))