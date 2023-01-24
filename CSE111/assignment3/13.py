class StudentDatabase:
    def __init__ (self,name,id):
        self.name=name
        self.id=id
        self.grades={}

    def calculateGPA(self,course,session):
        temp=[]
        for i in course:
            n=i.split(': ')
            temp.append(n)
        
        course_list=[]
        total_gpa=0
        
        for i in temp:
            total_gpa+=float(i[1])
        gpa=total_gpa/len(temp)

        for i in temp:
            course_list.append(i[0])
        self.grades.update({session:{tuple(course_list):gpa}})

    # def calculateGPA(self,clist,sem):
    #     self.grades[sem]={}
    #     grade=0

    #     for i in clist:
    #         c,g=i.split(': ')
    #         self.clist.append(c)
    #         grade+=float(g)
    #         self.gpa=grade/len(self.clist)
    
    def printDetails(self):
        print(f'Name: {self.name}')
        print(f'ID: {self.id}')

        for key,value in self.grades.items():
            print(f'Courses taken in {key}')
            for i,j in value.items():
                for c in i:
                    print(c)
                print('GPA %.2f'%j)


    

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'],
'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'],
'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()


