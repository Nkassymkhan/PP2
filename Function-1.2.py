def convertTemp(f):
    return (5 / 9) * (f - 32)

f = int(input("Enter a Fahrenheit temperature:"))

print('Centigrade temperature =', convertTemp(f))