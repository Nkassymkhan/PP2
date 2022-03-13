import re

s = input()

pattern = r'a.*b$'

if re.search(pattern, s):
    print("Found")
else:
    print("Not exist")
