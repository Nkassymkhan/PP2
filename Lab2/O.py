n = input()
l = {'ONE':'1',
'TWO':'2',
'THR':'3',
'FOU':'4',
'FIV':'5',
'SIX':'6',
'SEV':'7',
'EIG':'8',
'NIN':'9',
'ZER':'0'}
answer = ''
for i in range(len(n)):
    if n[i:i + 3] in l.keys():
        answer += l[n[i:i + 3]]
    elif n[i] == '+':
        answer += '+'
# print(ans)
result = str(sum(list(map(int, answer.split('+')))))
# print(res)
reverse_dict = {k:v for v,k in l.items()}
print(''.join(reverse_dict[i] for i in result))