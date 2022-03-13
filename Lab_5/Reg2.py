import re

s = input()

pattern = r'ab{2}'
pattern1 = r'ab{3}'

if re.search(pattern, s):
    print ('Found')
elif re.search(pattern1, s): 
    print ('Found')
else:
    print ('Not exist')
