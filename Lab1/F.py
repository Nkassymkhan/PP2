n = int(input())
l = []
for i in range (n):
    l.append(int(input()))

for i in range (n):
    if l[i] <= 10:
        print("Go to work!")
    elif l[i] <= 25:
        print("You are weak")
    elif l[i] <= 45:
        print("Okay, fine")
    elif l[i] > 45:
        print("Burn! Burn! Burn Young!")
