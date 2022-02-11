n = int(input())
l = []
for i in range (n):
    l.append(input())
for i in range (len(l)):
    s = l[i].endswith("@gmail.com")
    if s == True:
        print(l[i][:-10])

