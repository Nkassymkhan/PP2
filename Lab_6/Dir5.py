cars = ['Ford', 'BMW', 'Audi', 'Toyota', 'Lada'] 
 
with open(r'C:/Users/77079/Desktop/Programming/PP2/Lab_6/Task.txt', 'w') as fp: 
    for item in cars: 
        fp.write(f'{item} \n') 
