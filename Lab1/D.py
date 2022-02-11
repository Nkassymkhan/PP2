n = int(input())
z = str(input())

if z == 'k' :
    n /= 1024
    c = int(input())
elif z == 'b':
    n *= 1024
print(round(n, c))
