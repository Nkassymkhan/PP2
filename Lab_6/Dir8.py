import os 
path ='C:\\Users\\77079\\Desktop\\Programming\\PP2\\Lab_6\\delete.txt' 
 
 
print(path) 
 
if os.access(path, os.F_OK): 
 
    os.remove('del.txt') 
    print('File deleted') 
 
else: 
    print('File does not exist')