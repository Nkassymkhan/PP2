s = input()
sum = 0

for i in s:
    sum = sum + ord(i)
if sum >= 300:
    print("It is tasty!")
else: 
    print("Oh, no!")    