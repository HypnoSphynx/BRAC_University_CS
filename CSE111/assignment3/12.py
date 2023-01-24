class Account:
    def __init__(self,name='Default Acount',balance=0):
        self.name=name
        self.balance=balance
    def details(self):
        return("%s\n%.1f"%(self.name,self.balance))
    def withdraw(self,withdraw):
        temp=self.balance-withdraw

        if temp<=3070:
            print('Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.')
        else:
            self.balance=temp
            print('Withdraw successful! New balance is:')
            print(self.balance)
    
            


a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)
