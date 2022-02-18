class Uppercase:
    def __init__(self):
        self.string = ""
    def getString(self):
       self.string = input()
    
    def printString(self):
        print(self.string.upper())

S1 = Uppercase() 
S1.getString()
S1.printString()