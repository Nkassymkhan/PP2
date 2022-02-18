class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle():
    def __init__(self,length, width):
        self.length = length
        self.width = width
        super().__init__()
    
    def area(self):
        return self.length * self.width


R1 = Rectangle(int(input()), int(input()))
print(R1.area())