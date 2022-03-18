import os 
  
path = os.getcwd() 
print(os.path.exists(path)) 
 
print("File name of the path:") 
print(os.path.basename(path)) 
 
print("Dir name of the path:") 
print(os.path.dirname(path))

