class Cat:
    Number_of_cats=0
    def __init__(self,clr,position):
        self.clr=clr
        self.position=position
        Cat.Number_of_cats+=1

    @classmethod
    def no_parameter(cls):
        return cls('White','sitting')
    @classmethod
    def first_parameter(cls,val):
        return cls(val,'sitting')
    @classmethod
    def second_parameter(cls,val):
        return cls('Grey',val)

    def changeColor(self,val):
        self.clr=val
    
    def printCat(self):
        print(f'{self.clr} cat is {self.position}')

print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)
