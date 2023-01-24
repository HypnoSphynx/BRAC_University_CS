class Vaccine:
    def __init__(self,*args):
        self.name=args[0]
        self.country=args[1]
        self.days=args[2]


class Person:
    def __init__ (self,*args):
        self.vaccine=''
        self.dose_one=''
        self.dose_two=''
        if len(args)==2:
            self.name=args[0]
            self.age=args[1]
            self.citizen='General Citizen'
            self.vaccine=''

        else:
            self.name=args[0]
            self.age=args[1]
            self.citizen=args[2]

    def pushVaccine(self,*args):
        if self.citizen=='Student':
            if len(args)==1:
                self.vaccine=args[0].name
                self.dose_one='Given'
                self.dose_two=f'Please come after {args[0].days} days'
                print(f'1st dose done for{self.name}')
            else:
                if args[0].name==self.vaccine:
                    self.vaccine=args[0].name
                    self.dose_one='Given'
                    self.dose_two='Given'
                    print(f'2nd dose done for {self.name}')
                else:
                    print(f'Sorry {self.name}, you can’t take 2 different vaccines')
        else:
            if self.age>=25:
                if len(args)==1:
                    self.vaccine=args[0].name
                    self.dose_one='Given'
                    self.dose_two=f'Please come after {args[0].days} days'
                    print(f'1st dose done for{self.name}')
                else:
                    if args[0].name==self.vaccine:
                        self.vaccine=args[0].name
                        self.dose_one='Given'
                        self.dose_two='Given'
                        print(f'2nd dose done for {self.name}')
                    else:
                        print(f'Sorry {self.name}, you can’t take 2 different vaccines')
            else:
                print(f'Sorry {self.name}, Minimum age for taking vaccines is 25 years now.')
    def showDetail(self):
            print(f'Name: {self.name}')
            print(f'Vaccine: {self.vaccine}')
            print(f'1st dose: {self.dose_one}')
            print(f'2nd dose: {self.dose_two}')           


astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")


        






