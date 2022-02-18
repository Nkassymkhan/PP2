def unique(ulist, list):
    for i in list:
        if i not in ulist:
            ulist.append(i)
    return ulist
list = list(map(int, input().split()))
ulist = []
print(unique(ulist, list))