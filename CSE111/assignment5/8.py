class Coordinates:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.tuple=(x,y)

    def __sub__(obj1,obj2):
        x=obj1.x-obj2.x
        y=obj1.y-obj2.y

        obj=Coordinates(x,y)
        return obj
    
    def __mul__(obj1,obj2):
        x=obj1.x*obj2.x
        y=obj1.y*obj2.y

        obj=Coordinates(x,y)
        return obj
    
    def detail(self):
        return self.tuple
    
    def __eq__(obj1,obj2):
        
        if obj1.x==obj2.x and obj1.y==obj2.y:
            return 'The calculated coordinates are the same.'
        else:
            return 'The calculated coordinates are NOT the same.'
p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))

p4 = p1 - p2 
print(p4.detail())

p5 = p1 * p2
print(p5.detail())

point_check = (p4 == p5)
print(point_check)
