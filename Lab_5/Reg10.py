import re

pattern = r"(.+?)([A-Z])"

def snake(s):
    return s.group(1).lower() + "_" + s.group(2).lower()

words = input().splitlines()

results = [re.sub(pattern, snake, w, 0) for w in words]

print(results)