import re

s = input()

print(''.join(x.capitalize() or '_' for x in s.split('_')))