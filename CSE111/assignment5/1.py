class Exam:
    def __init__(self,mark):
        self.mark=mark

    def __add__(self,other):
        obj=Exam(self.mark+other.mark)
        return obj    


Q1 = Exam(int(input("Quiz 1 (out of 10): ")))
Q2 = Exam(int(input("Quiz 2 (out of 10): ")))
Lab = Exam(int(input("Lab (out of 30): ")))
Mid = Exam(int(input("Mid (out of 20): ")))
Final = Exam(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))
