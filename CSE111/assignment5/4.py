class Color:
    def __init__(self,color):
        self.clr=color
        self.lst=[['red','yellow','Orange'],['red','blue','Violet'],['yellow','blue','Green']]
        
    
    def __add__(self,other):
        clr=''
        for i in self.lst:
            if self.clr in i and other.clr in i:
                clr=i[2]
        obj=Color(clr)
        return obj

        


C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)

