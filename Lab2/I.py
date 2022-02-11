n = int(input()) 
l = [] 
l1 = [] 
l2 = [] 
for i in range(n): 
    disc = input() 
    if disc[0] == "1": 
        l.append(disc[2:]) 
    elif disc[0] == "2": 
        l1.append(disc[:2]) 

s = l1.count("2") 
l2.append(l[:s]) 
for j in l2: 
    print(*j)