file = open('C:/Users/77079/Desktop/Programming/PP2/Lab_6/Lines.txt','r')  
cnt  = 0 
text = file.read()  
list = text.split("\n")  
 
for x in list:  
    if x:  
        cnt += 1 
   
print("lines in txt file:", cnt )