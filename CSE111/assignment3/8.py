class Student:
    def __init__(self,*args):
        self.effort=0
        if len(args)==2:
            self.name=args[0]
            self.id=args[1]
            self.dept="CSE"
        else:
            self.name=args[0]
            self.id=args[1]
            self.dept=args[2]
    def dailyEffort(self,value):
        self.effort+=value

    def printDetails(self):
        print(f'Name:{self.name}')
        print(f'ID: {self.id}')
        print(f'Department:{self.dept}')
        print(f'Daily Effort: {self.effort} hour(s)')
        if self.effort<=2:
            print('Suggestion: Should give more effort!')
        elif self.effort<=4:
            print('Suggestion: Keep up the good work!')
        else:
            print('Suggestion: Excellent! Now motivate others.')

harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
