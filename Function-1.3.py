from tkinter import Y


def solve(numheads, numlegs):
    chickens = (numlegs - 2*numheads)/2                #x+y = 35 x = 35 - y
    rabbits =(numheads - chickens)                     #2x + 4y = 94   
    if chickens % 2 == 0:
        return round(chickens), round(rabbits)         #2*35 - 2*y + 4*y = 94 
    else: 
        return 'Invalid'                               #70 + 2*y = 94
                                                       #2*y = 24
                                                       # y = 12  
numheads = int(input())
numlegs = int(input())

print(solve(numheads, numlegs))                        # x = 35 - 12 = 23 

