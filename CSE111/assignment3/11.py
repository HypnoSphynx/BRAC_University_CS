class TaxiLagbe:
    def __init__(self,id,area):
        self.id=id
        self.area=area
        self.psngr_lst=[]
        self.total_fare=0
    
    def addPassenger(self,*args):
        
        if len(self.psngr_lst)<4:
            for i in args:
                temp=i.split('_')
                self.psngr_lst.append(temp[0])
                print(f'Dear {temp[0]}, Welcome to TaxiLagbe.')
                self.total_fare+=(int(temp[1]))
        else:
            print('Taxi Full, No more passengers can be added')
            

    def printDetails(self):
        print(f'Trip info for Taxi number: {self.id}')
        print(f'This taxi can cover only {self.area} area.')
        print(f'Total passengers: {len(self.psngr_lst)}')
        print('Passenger list:')

        for i in range(len(self.psngr_lst)):
            if i==len(self.psngr_lst)-1:
                print(self.psngr_lst[i])
            else:
                print(self.psngr_lst[i],end=',')

        print(f'Total collected fare: {self.total_fare}')


taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()
