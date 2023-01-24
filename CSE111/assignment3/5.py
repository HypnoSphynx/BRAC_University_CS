class UberEats:
    def __init__(self,*args):
        self.name=args[0]
        self.number=args[1]
        self.location=args[2]
        self.items={}
        self.taka=0
        print(f'{self.name}, Welcome to Uber Eats')
        

    def add_items(self,*args):
        self.items.update({args[0]:args[3]})
        self.items.update({args[1]:args[2]})
        self.taka=args[2]+args[3]


    def print_order_detail(self):
        print(f'User Details: Name:{self.name}, Phone:\n{self.number}, Address:{self.location}')
        print(f'Orders: {self.items}')
        print(f'Total Paid Amount: {self.taka}')

        



order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())
