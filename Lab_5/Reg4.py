import re

s = input()

pattern = r'[A-Z]+[a-z]+$'

if re.search(pattern, s):
    print("Found")
else:
    print("Not exist")
