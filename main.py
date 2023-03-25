# OOP programming class

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self,rectangle):
        if rectangle.lowleft.x>self.x <rectangle.upperight.x and rectangle.lowleft.y >self.y <rectangle.upperight.y:
            return True
        else:
            return False

    def distance_from_point(self,x,y):
        return ((self.x - x)**2 + ((self.y-y)**2))**0.5


point1 = Point(1,1)
print(point1.distance_from_point(3,3))

class Recetangle:

    def __init__(self,lowleft,upperight):
        self.lowleft = lowleft
        self.upperight = upperight

# pointx = Point(6,7)
# rectanglex = Recetangle(Point(5,6),Point(7,9))
#
# print(pointx.falls_in_rectangle(rectanglex))
#

from random import randint
rectangle = Recetangle(Point(randint(0,9),randint(0,9)),Point(randint(10,19),randint(10,19)))

print(rectangle.lowleft.x,rectangle.lowleft.y)
