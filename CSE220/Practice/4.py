class Node:
    def __init__(self,node):
        self.element=node
        self.nelement=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printelement(self):
        printval=self.head
        while printval is not None:
            print(printval.element)
            printval=printval.nelement

    def AtBegining(self,newdata):
        NewNode = Node(newdata)

        NewNode.nelement = self.head
        self.head = NewNode
    
    
    def AtEnd(self,newdata):
        NewNode=Node(newdata)
        if self.head is None:
            self.head=NewNode
            return
        laste=self.head
        while(laste.nelement):
            # print(laste.nelement)
            laste=laste.nelement
        laste.nelement=NewNode


list=Linkedlist()
list.head=Node(1)
e2=Node(2)
e3=Node(3)
list.head.nelement=e2
e2.nelement=e3

# list.AtEnd(5)
print(e3.nelement)


# list.printelement()