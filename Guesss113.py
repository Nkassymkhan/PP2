import random

def guess(n, num, inum, cnt = 0):
  while cnt < 20:
    if num == inum:
        print(f'Good job, {n}! You guessed my number in {cnt} guesses!')
        break
    elif num > inum:
        print(f'Your guess is too low.\nTake a guess.')
        cnt += 1
        inum = int(input())
    elif num < inum:
         print(f'Your guess is too high.\nTake a guess.')
         cnt += 1
         inum = int(input())
n = input("Hello! What is your name?\n")
num = random.randint(1, 20)
inum = int(input(f'Well, {n}, I am thinking of a number between 1 and 20.\nTake a guess.\n'))
guess(n, num, inum, cnt = 0)