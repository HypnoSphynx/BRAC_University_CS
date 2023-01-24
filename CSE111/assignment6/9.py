class Student:
    brac=0
    other=0
    total=0
    def __init__(self,name,dept,ins='BRAC University'):
        self.name=name
        self.dept=dept
        self.ins=ins
        if ins== 'BRAC University':
            Student.brac+=1  
        else:
            Student.other+=1
        Student.total=Student.brac+Student.other
    def individualDetail(self):
        print(f'Name: {self.name}')
        print(f'Deparment: {self.dept}')
        print(f'Institution: {self.ins}')
    @staticmethod
    def printDetails():
        print(f'Total Student= {Student.total}')
        print(f'BRAC University Student(s)= {Student.brac}')
        print(f'Other instituition Student(s)= {Student.other}')
    @classmethod
    def createStudent(cls,name,dept,ins='BRAC University'):
        return cls(name,dept,ins)

        

Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
