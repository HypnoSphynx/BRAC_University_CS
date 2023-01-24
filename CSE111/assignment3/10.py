class Author:
    def __init__(self,*args):
        if len(args)==0:
            self.name='Default'
            self.list=[]
            
        elif len(args)==1:
            self.name=args[0]
            self.list=[]
            print(f'Author name: {self.name}')

        else:
            self.name=args[0]
            self.list=args[1::]
            print(f'Author name: {self.name}')

    def addBooks(self,*args):
        for i in args:
            self.list.append(i)

    def changeName(self,name):
        self.name=name
        print(self.name)

    def printDetails(self):
        print('List of books:')
        for i in self.list:
            print(i)
auth1 = Author('Humayun Ahmed')
print('--------')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
print("===================")
auth2.changeName('Mario Puzo')
print('--------')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
auth2.printDetails()
print("===================")
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
print('--------')
auth3.printDetails()
