# Write your code here
class Shape:
    def __init__ (self,name,val1,val2):
        self.name=name
        self.val1=val1
        self.val2=val2
    def area(self):
        if self.name=='Triangle':
            area=.5*self.val1*self.val2
            print(area)
        elif self.name=='Square':
            area=self.val1*self.val2
            print(area)
        elif self.name=='Rectangle':
            area=self.val1*self.val2
            print(area)
        elif self.name=='Rhombus':
            area=(self.val1*self.val2)/2
            print(area)
        else:
            print('Shape Unknown')
triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()
