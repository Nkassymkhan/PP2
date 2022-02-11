l = list()
while True:
    date = input()
    if date == '0':
        break
    else:
        d = date.split()
        l.append(d[2] + ' ' + d[1] + ' ' + d[0]) 
for date in sorted(l):
    date = date.split()
    print(f'{date[2]} {date[1]} {date[0]}')