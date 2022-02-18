def prime(num):   
    prime = True
    is_prime = lambda a, b: a % b == 0
    for i in range (2, num):
        if(is_prime(num, i)):
            prime = False
            break
    return prime

n = int(input())
l = []
for i in range(n):
    s = int(input())
    l.append(int(i))
l1 = list(filter(prime, l))
print(l1)