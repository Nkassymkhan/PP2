f, n = map(int, input().split())

def isprime(f): 
        for i in range(2,f):  
            if (f % i) == 0:  
                return False
        else:
                return True
def iseven(n):
        if (n % 2 == 0):
            return True
        else:
            return False

if isprime(f) and f < 500 and iseven(n):
    print("Good job!")
else:
    print("Try next time!")