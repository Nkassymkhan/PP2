n, f = map(int, input().split())
l = []
if len(l) == 1:
    int(input())
XOR = int()
for i in range (0, n):
    l.append(f + 2 * i)
    XOR ^= l[i]
print(XOR)
    
