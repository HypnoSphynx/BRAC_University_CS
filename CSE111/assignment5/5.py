import math
class Circle:
    def __init__(self,radius):
        self.__radius=radius

    def __add__(self,value):
        val=self.__radius+value.__radius
        obj=Circle(val)
        return obj
    
    def getRadius(self):
        return self.__radius
    
    def area(self):
        area=math.pi*(self.__radius)**2
        return area


c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
 
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
 
c3 = c1 + c2 
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())
