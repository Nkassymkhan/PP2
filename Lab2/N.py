l = []
l1 = []
l.append((int(input())))
while(l[len(l) - 1] != 0):
    l.append(int(input()))

for i in range(int((len(l) - 1) / 2)):
    l1.append(l[i] + l[len(l) - 2 - i])
    
if(len(l) % 2 == 0):
    l1.append(l[int((len(l)) / 2 ) - 1])

print(*l1)