def strong(n):
    s = ['()', '{}', '[]']
    while any(x in n for x in s):
        for i in s:
            n = n.replace(i, '')
    return not n


n = input()
print("Yes"
      if strong(n) else "No")