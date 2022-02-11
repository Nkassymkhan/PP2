n = str(input())
x = input()
s = []
cnt = 0
for i in range (len(n)):
    if n[i] == x:
       s.append(i)
       cnt+=1
if cnt == 1:
    print(s[0])   
else:
    print(s[0], s[-1])
