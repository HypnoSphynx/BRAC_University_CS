class Team:
    def  __init__(self,country=None):
        self.__team=country
        self.__lst=[]

    def setName(self,value):
        self.__team=value

    def addPlayer(self,value):
        if value not in self.__lst:
            self.__lst.append(value.name)

    def printDetail(self):
        print('=====================')
        print(f'Team: {self.__team}')
        print('List of players')
        print(self.__lst)
        print('=====================')
        

class Player:
    def __init__(self,name):
        self.name=name
    

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
