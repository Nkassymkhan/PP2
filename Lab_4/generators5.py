def decreasing(n):
    for i in reversed(range(n)):
        yield i

n = int(input())
for x in decreasing(n):
    print(x)