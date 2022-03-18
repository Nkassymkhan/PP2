from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args) 
a = int(input())
b = int(input())

print(f'Square root of {a} after {b} miliseconds:', (delay(lambda x: math.sqrt(x), a, b)))