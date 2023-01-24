class SultansDine:
    branch=0
    totalsell=0
    lst=[]
    def __init__(self,location):
        self.location=location
        self.quantity=0
        self.branch_sell=0
        SultansDine.branch+=1

    def sellQuantity(self,val):
        self.quantity=val
    
    def branchInformation(self):
        print(f'Branch Name: {self.location}')
        if self.quantity < 10:
            self.branch_sell = self.quantity * 300
        elif self.quantity < 20:
            self.branch_sell = self.quantity * 350
        else:
            self.branch_sell = self.quantity * 400
        print(f'Branch sell:{self.branch_sell} Tk')

        SultansDine.lst.append([self.location,self.branch_sell])
        SultansDine.totalsell+=self.branch_sell
           
    
    @classmethod
    def details(cls):
        print(f'Total Number of branche(s):{cls.branch}')
        print(f'Total sell: {cls.totalsell} taka')
        for i in cls.lst:
            print(f'Branch Name: {i[0]}, Branch Sell: {i[1]}')
            branchsell=(i[1]/cls.totalsell)*100
            print("Branch consists of total sell's: %.2f"%branchsell,"%")
            




SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()


