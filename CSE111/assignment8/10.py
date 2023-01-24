class Department:
    def __init__(self, s):
        self.semester = s
        self.name = "Default"
        self.id = -1
        
    def student_info(self):
        print("Name:", self.name)
        print("ID:", self.id) 
        
    def courses(self, c1, c2, c3):
        print("No courses Approved yet!")

class CSE(Department):
    def __init__(self,name,id,semester):
        super().__init__(semester)
        self.name=name
        self.id=id
    def courses(self,*args):
        if len(args)==0:
            super().courses(None,None,None)
        print('Courses Approved to this EEE student in Spring2018 semester:')
        print(args[0])
        print(args[1])
        print(args[2])
class EEE(Department):
    def __init__(self,name,id,semester):
        super().__init__(semester)
        self.name=name
        self.id=id
    def courses(self,*args):
        if len(args)==0:
            super().courses(None,None,None)
        else:
            print('Courses Approved to this EEE student in Spring2018 semester:')
            for i in args:
                print(i)



s1 = CSE("Rahim", 16101328,"Spring2016")
s1.student_info()
s1.courses("CSE110", "MAT110", "ENG101")
print("==================")
s2 = EEE("Tanzim", 18101326, "Spring2018")
s2.student_info()
s2.courses("Mat110", "PHY111", "ENG101")
print("==================")
s3 = CSE("Rudana", 18101326, "Fall2017")
s3.student_info()
s3.courses("CSE111", "PHY101", "MAT120")
print("==================")
s4 = EEE("Zainab", 19201623, "Summer2019")
s4.student_info()
s4.courses("EEE201", "PHY112", "MAT120")
