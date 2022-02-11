from audioop import reverse


n = int(input())
d = {}
for i in range(n):
    name, cash = input().split()
    cash = int(cash)
    d[name] = d.get(name, 0) + cash
max = max(d.values())
for name, cash in (d.items(), key=lambda x:(x[1])):
    if max - d[name] == 0:
        print(f"{name} is lucky!")
    else:
        print(f"{name} has to receive {max - d[name]}")