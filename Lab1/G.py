n = str(input())

def fbtd (n, e = 1):
    if int(n) == 0:
        return 0
    else: 
        s = int(n) % 10
        n = int(n // 10)
        s = s * e
        return s + fbtd(int(n), e * 2)
print (fbtd(int (n)))