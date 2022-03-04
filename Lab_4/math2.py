def areatrp(h, b1, b2):
    return h*(b1 + b2)/2

h = int(input('Height: '))
b1 = int(input('Base 1: '))
b2 = int(input('Base 2: '))

print('Area of Trapezoid is:', areatrp(h, b1, b2))