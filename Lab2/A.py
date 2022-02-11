n = input().split() 
l = [] 
s = 0
for i in range (len(n)): 
    l.append(int(n[i])) 
for i in range (len(n)): 
    if s >= i: 
        if l[i] + i >= len(n) - 1: 
            print(1) 
            exit() 
        elif l[i] + i > s: 
            s = l[i] + i 
    else: 
        break
if s < len(n) - 1: 
    print(0)