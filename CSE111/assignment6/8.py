import math
class Cylinder:
    radius=5
    height=18
    def __init__(self,radius,height):
        self.radius=Cylinder.radius
        self.height=Cylinder.height
        print(f'Default radius={self.radius} Default Height={self.height}')
        self.radius=radius
        self.height=height
        Cylinder.radius=radius
        Cylinder.height=height
        print(f'Updated radius={self.radius} Updated Height={self.height}')

    @staticmethod
    def area(val1,val2):
        area=(2*(math.pi)*(val1**2))+2*(math.pi)*(val2)*(val1)
        print(f'Area={area}')
    @staticmethod
    def volume(val1,val2):
        vol=(math.pi)*(val1**2)*(val2)
        print(f'Volume={vol}')
    @classmethod
    def swap(cls,val1,val2):
        return cls(val2,val1)
    @classmethod
    def changeFormat(cls,val):
        lst=val.split('-')
        return cls(float(lst[0]),float(lst[1]))


c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)