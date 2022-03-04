from cmath import tan, pi


def arearegpol(n, l):
    return ((n * l**2)/(4 * tan(pi/n)))

n = int(input('Number of slides: '))
l = int(input('Length: '))

print('Area of Regular Polygon is:', arearegpol(n, l)) 