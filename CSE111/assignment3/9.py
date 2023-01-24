class Batsman:
    def __init__(self,*args):
        if len(args)==2:
            self.name='New Batsman'
            self.run=args[0]
            self.balls=args[1]
        else:
            self.name=args[0]
            self.run=args[1]
            self.balls=args[2]
    def battingStrikeRate(self):
        strike=(self.run/self.balls)*100
        return strike
    def printCareerStatistics(self):
        print(f'Name: {self.name}')
        print(f'Runs scored:{self.run}, Balls Faced: {self.balls}')
    def setName(self,name):
        self.name=name

b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())
