n = int(input()) 
 
m =[[0 for i in range(n)] for j in range(n)] 
 
for i in range(n): 
    for j in range(n): 
        if( i== 0 or j == 0): 
            m[i][j] = i + j 
        elif(i == j):  
            m[i][j] = i * j 
 
for i in range(n): 
    for j in range(n): 
        print(m [i][j], end=' ') 
    print()