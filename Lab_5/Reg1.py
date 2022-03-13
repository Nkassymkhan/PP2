import re

s = input()
 
pattern = r'ab*'

if re.search(pattern, s):
    print ('Found')
else:
    print ('Not exist')
