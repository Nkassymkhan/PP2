from math import pi

def degtorad(d):
    return d * (pi/180)

d = int(input('Degree: '))
print('Radian:', degtorad(d))