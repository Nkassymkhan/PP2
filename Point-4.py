import math


class Point:
    def __init__(self, xcor, ycor):
        self.xcor = xcor
        self.ycor = ycor

    def show(self):
        print (self.xcor, self.ycor)

    def move(self):
        self.xcor = int(input())
        self.ycor = int(input())
    
    def dist(self, P2):
        return math.sqrt((self.xcor + P2.xcor)**2 + (self.ycor + P2.ycor)**2)



P1 = Point(int(input()), int(input()))
P2 = Point(int(input()), int(input()))


print(P1.dist(P2))
