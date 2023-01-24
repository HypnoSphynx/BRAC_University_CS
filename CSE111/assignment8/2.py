class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)

class ComplexNumber(RealNumber):
    def __init__(self,val1,val2):
        if type(val1)==int:
            super().__init__(val1)
        else:
            super().__init__(val1.number)
        self.imagin=val2
    def __add__(obj1,obj2):
        return ComplexNumber(super().__add__(obj2),obj1.imagin+obj2.imagin)
    def __sub__(obj1,obj2):
        return ComplexNumber(super().__sub__(obj2),obj1.imagin-obj2.imagin)


    def __str__(self):
        if self.imagin>0:
            return f'{super().__str__()} + {str(self.imagin)}i'   
        else:
            temp=-1*self.imagin
            return f'{super().__str__()} - {str(temp)}i'



r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2 #ComplexNumber(3,5)
print(cn3)
cn4 = cn1 - cn2
print(cn4)
