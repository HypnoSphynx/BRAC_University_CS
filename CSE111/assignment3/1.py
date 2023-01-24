class Patient:
    
    def __init__ (self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height/100
    def printDetails(self):
        print(self.name)
        print(self.age)
        print(self.weight,'kg')
        print(self.height,'cm')
        bmi=self.weight/self.height**2
        print('BMI:',bmi)
p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()
