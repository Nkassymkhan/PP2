from math import pi

def volume(r):
    return r**3 * 4/3 * pi

r = int(input("Enter radius:"))
print("Volume of sphere=", volume(r))