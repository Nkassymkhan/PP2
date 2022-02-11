n = int(input())  
l = list(map(int,input().strip().split()))[:n] 
l.sort(reverse=True)
print(l[0]*l[1])