class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n

class LinkedList:
  
    def __init__(self, a):
        if type(a)==list:
            self.head=Node(a[0],None)
            tail=self.head

            for i in range(1,len(a)):
                newnode=Node(a[i],None)
                tail.next=newnode
                tail=newnode
        else:
            self.head=a
    def traverseList(self):
        s = ''
        temp = self.head
        while temp != None:
            if temp.next != None:
                s += str(temp.element) + " "
            else:
                s += str(temp.element)
            temp = temp.next
        return s
    def countNode(self):
        temp=self.head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        return count

    def rotateRight(self):
        count=0
        tail=self.head
        temp=None
        while count<=(self.countNode()-2):
            if count==(self.countNode()-2):
                temp=tail.next
                tail.next=None
            count+=1
            tail=tail.next
        self.head=Node(temp.element,self.head)
        

print("////// Test 12 //////")
a9 = [10,20,30,40]
h9 = LinkedList(a9) # uses the constructor where a is an built in list
print(h9.traverseList()) # This should return: 10 20 30 40

print('------------------------------')    
# Rotates the list to the right by 1 position.
h9.rotateRight()
print(h9.traverseList()) # This should return: 40 10 20 30


    