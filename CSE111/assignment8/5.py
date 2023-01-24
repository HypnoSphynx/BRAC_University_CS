class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
        
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"

class ScienceExam(Exam):
    def __init__(self,*args):
        super().__init__(args[0])
        self.time=args[1]
        self.sub_lst=[]
        for i in range(len(args)):
            if i>1:
                self.sub_lst.append(args[i])
        self.total_sub=2+len(self.sub_lst)

    def __str__(self):
        return f'Marks:{self.marks} Time:{self.time} minutes Number of Parts:{self.total_sub} '

    def examSyllabus(self):
        return f"{super().examSyllabus()}, {', '.join(self.sub_lst)}"

    def examParts(self):
        string=super().examParts()
        for i in range(len(self.sub_lst)):
            string=string+'Part '+str(i+3)+' - '+self.sub_lst[i]+'\n'
        return string



    
    
    
engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================') 
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())
