class Assassin:
    id=0
    def __init__(self,name,rate):
        self.name=name
        self.rate=rate
        Assassin.id+=1
        self.id=Assassin.id
    
    @classmethod
    def failureRate(cls,name,rate):
        f_rate=100-int(rate)

        obj=cls(name,f_rate)
        return obj
    @classmethod
    def failurePercentage(cls,name,rate):
        f_rate=100-int(rate[:len(rate)-1:])

        obj= cls(name,f_rate)
        return obj
    
    def printDetails(self):
        print(f'Name: {self.name}')
        print(f'Success rate: {self.rate}%')
        print(f'Total number of Assassin: {self.id}')



john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()
