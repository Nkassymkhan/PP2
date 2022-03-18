s = input() 
upper, lower = 0,0 
 
for i in s: 
    if (i.islower()): 
        upper = upper + 1                  
    elif (i.isupper()): 
        lower = lower + 1    
           
print('Lower case letters: ', upper) 
print('Upper case letters: ', lower)