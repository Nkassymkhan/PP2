import os 
 
direc = os.getcwd() 
 
for item in os.listdir(direc):  
  joined = os.path.join(direc, item) 
  print('Exist:', os.access(joined, os.F_OK)) 
  print('Readable:', os.access(joined, os.R_OK))  
  print('Writable:', os.access(joined, os.W_OK)) 
  print('Executable:', os.access(joined, os.X_OK))