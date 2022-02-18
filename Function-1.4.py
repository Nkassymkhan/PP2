def filter_prime(n):
   if n == 2 or n == 3:
        return True
   if n % 2 == 0 or n < 1:
        return False
   #for i in range(2, n):
   for i in range(2, int(n**1/2)+1,2):   
        if n % i == 0:
            return False   
   return True

s = input()
l = []
l1 = s.split(" ")

for x in l1:
    l.append(int(x))
l1 = list(filter(filter_prime, l))
print(l1)