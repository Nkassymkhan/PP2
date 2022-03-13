import re

s = input()

pattern = r'[a-z]+_[a-z]+$'

if re.search(pattern, s):
    print("Found")
else:
    print("Not exist")

    