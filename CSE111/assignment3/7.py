class Cat:
    def __init__ (self,*args):
        if len(args)==0:
            self.color='White'
            self.position='sitting'
        elif len(args)==1:
            self.color=args[0]
            self.position='sitting'
        else:
            self.color=args[0]
            self.position=args[1]

    def printCat(self):
        print(self.color, 'cat is', self.position)
    def changeColor(self,val):
        self.color=val

c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()