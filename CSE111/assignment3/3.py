

class Calculator:
    def __init__ (self,*args):
        if len(args)==0:
            print('Calculator is ready')
        
    def calculate(self,*args):
        self.val1=args[0]
        self.val2=args[1]
        self.operator=args[2]
        
        if self.operator=='+':
            self.val=self.val1+self.val2
        elif self.operator=='-':
            self.val=self.val1-self.val2
        elif self.operator=='*':
            self.val=self.val1*self.val2
        elif self.operator=='/':
            self.val=self.val1/self.val2
        return self.val
    
    def showCalculation(self):
        return self.val

c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()
