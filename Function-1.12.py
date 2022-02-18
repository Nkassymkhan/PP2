def histogram(list):
    for i in range(len(list)):
        print ('*' * list[i])
    return

list = list(map(int, input().split()))
histogram(list)