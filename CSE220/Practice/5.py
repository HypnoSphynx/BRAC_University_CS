import fhm_unittest as unittest
class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n

# To you coding in this cell
class LinkedList:
  
  def __init__(self, a):
      if type(a) == list:
          self.head = Node(a[0],None)
          Tail = self.head
          for i in range(1,len(a)):
              newNode = Node(a[i],None)
              Tail.next = newNode
              Tail = Tail.next
      else:
          self.head = a
  
  # Traverse elements in the list.
  # This method is done for you. Do not change this method.
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
  
  # Count the number of nodes in the list and return the total number
  def countNode(self):
    count=0
    temp=self.head
    while temp!=None:
        count+=1
        temp=temp.next
    return count
  
  # returns the reference of the Node at the given index. For invalid index return None.
  def nodeAt(self, idx):
    temp = self.head
    count=0
    output=0
    while count<=idx:
        output=temp
        temp = temp.next
        count+=1
    return output
  
  
  # returns the element of the Node at the given index. For invalid idx return None.
  def get(self, idx):
    temp = self.head
    count=0
    output=0
    while count<=idx:
        output=temp.element
        temp = temp.next
        count+=1
    return output
  
  # updates the element of the Node at the given index. 
  # Returns the old element that was replaced. For invalid index return None.
  # parameter: index, element
  def set(self, idx, elem):
        if idx>self.countNode():
            print('Invalid index')
        else:
            temp = self.head
            count=0
            temp1=0
            while count<=idx:
                if count==idx:
                    temp1=temp.element
                    temp.element=elem
                    return temp1
                temp = temp.next
                count+=1
            


  # returns the index of the Node containing the given element.
  # if the element does not exist in the List, return -1.
  def indexOf(self, elem):
        temp = self.head
        count=0
        output=None
        while temp!=None:
            if temp.element==elem:
                return count
            elif count==self.countNode():
                return -1
            temp = temp.next
            count+=1
        
  
  # returns true if the element exists in the List, return false otherwise.
  def contains(self, elem):
    temp = self.head
    while temp!=None:
        if temp.element==elem:
            return True
        temp = temp.next

    

  # Makes a duplicate copy of the given List. Returns the reference of the duplicate list.
  def copyList(self):
    array=[None]*self.countNode()
    temp=self.head
    for i in range(len(array)):
        array[i]=temp.element
        temp=temp.next
    
  def median(self):
        even_count=None
        odd_count=None
        output=None
        if self.countNode()%2!=0:
            odd_count=(self.countNode()//2)
        else:
            odd_count=(self.countNode()+1)//2
            even_count=(self.countNode()-1)//2
        if even_count==None:
            output=self.get(odd_count)
        else:
            output=(self.get(odd_count)+self.get(even_count))/2
        return output


  # Makes a reversed copy of the given List. Returns the head reference of the reversed list.
  def reverseList(self):
    # To Do
    pass # Delete this line
  
  # inserts Node containing the given element at the given index
  # Check validity of index. If invalid then print "Invalid Index"
  def insert(self, elem, idx):
    # To Do
    pass # Delete this line

  # removes Node at the given index. returns element of the removed node.
  # Check validity of index. return None if index is invalid.
  def remove(self, idx):
    # To Do
    pass # Delete this line
  
  # Rotates the list to the left by 1 position.
  def rotateLeft(self):
    # To Do
    pass # Delete this line
  
  
  # Rotates the list to the right by 1 position.
  def rotateRight(self):
    # To Do
    pass # Delete this line
# Do not modify this cell. Run this for test your written code.
print("////// Test 01 //////")
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1) # Creates a linked list using the values from the array
# head will refer to the Node that contains the element from a[0]

returned_value = h1.traverseList() # This should return: 10 20 30 40
unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')
retured_value = h1.countNode() # This should return: 4
unittest.output_test(retured_value, 4)

print("////// Test 02 //////")
# returns the reference of the Node at the given index. For invalid idx return None.
myNode = h1.nodeAt(1)
retured_value = myNode.element # This should return: 20. In case of invalid index This will generate an Error.
unittest.output_test(retured_value, 20)
    
print("////// Test 03 //////")
# returns the element of the Node at the given index. For invalid idx return None.
val = h1.get(2)  # This should return: 30. In case of invalid index This will print None.
unittest.output_test(val, 30)

print(h1.traverseList()) 
print("median    ", h1.median())
print("////// Test 04 //////")
    
# updates the element of the Node at the given index. 
# Returns the old element that was replaced. For invalid index return None.
# parameter: index, element
         
replaced_value = h1.set(1,85) # This should return: 20
unittest.output_test(replaced_value, 20)
print('------------------------------')
returned_value = h1.traverseList() # This should return: 10 85 30 40
unittest.output_test(returned_value, '10 85 30 40')
print('------------------------------')
replaced_value = h1.set(15,85) # This should return: None
unittest.output_test(replaced_value, None)
print('------------------------------')
returned_value = h1.traverseList() # This should return: 10 85 30 40
unittest.output_test(returned_value, '10 85 30 40')
    
print("////// Test 05 //////")
# returns the index of the Node containing the given element.
# if the element does not exist in the List, return -1.
index = h1.indexOf(40) # This should return: 3. In case of element that doesn't exists in the list this will print -1.
unittest.output_test(index, 3)
    
print("////// Test 06 //////")
# returns true if the element exists in the List, return false otherwise.
ask = h1.contains(40)  # This should return: True.
unittest.output_test(ask, True)
    
    
print("////// Test 07 //////")
a2 = [10,20,30,40,50,60,70]
h2 = LinkedList(a2) # uses theconstructor where a is an built in list
print(h2.traverseList()) 
print("median    ", h2.median())
returned_value = h2.traverseList() # This should return: 10 20 30 40 50 60 70  
unittest.output_test(returned_value, '10 20 30 40 50 60 70')
print('------------------------------')
# Makes a duplicate copy of the given List. Returns the head reference of the duplicate list.
copyH=h2.copyList() # Head node reference of the duplicate list
h3 = LinkedList(copyH) # uses the constructor where a is head of a linkedlist 
returned_value = h3.traverseList() # This should return: 10 20 30 40 50 60 70  
unittest.output_test(returned_value, '10 20 30 40 50 60 70')
    
print("////// Test 08 //////")
a4 = [10,20,30,40,50]
h4 = LinkedList(a4) # uses the constructor where a is an built in list
returned_value = h4.traverseList() # This should return: 10 20 30 40 50  
unittest.output_test(returned_value, '10 20 30 40 50')
print('------------------------------')
# Makes a reversed copy of the given List. Returns the head reference of the reversed list.
revH=h4.reverseList() # Head node reference of the reversed list
h5 = LinkedList(revH) # uses the constructor where a is head of a linkedlist 
returned_value = h5.traverseList() # This should return: 50 40 30 20 10  
unittest.output_test(returned_value, '50 40 30 20 10')
    
print("////// Test 09 //////")
a6 = [10,20,30,40]
h6 = LinkedList(a6) # uses theconstructor where a is an built in list
returned_value = h6.traverseList() # This should return: 10 20 30 40  
unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')   
# inserts Node containing the given element at the given index. Check validity of index.
h6.insert(85,0)
returned_value = h6.traverseList() # This should return: 85 10 20 30 40  
unittest.output_test(returned_value, '85 10 20 30 40')
print('------------------------------')
h6.insert(95,3)
returned_value = h6.traverseList() # This should return: 85 10 20 95 30 40  
unittest.output_test(returned_value, '85 10 20 95 30 40')
print('------------------------------')
h6.insert(75,6)
returned_value = h6.traverseList() # This should return: 85 10 20 95 30 40 75
unittest.output_test(returned_value, '85 10 20 95 30 40 75')
    
    
    
print("////// Test 10 //////")
a7 = [10,20,30,40,50,60,70]
h7 = LinkedList(a7) # uses theconstructor where a is an built in list
returned_value = h7.traverseList() # This should return: 10 20 30 40 50 60 70  
unittest.output_test(returned_value, '10 20 30 40 50 60 70')
print('------------------------------')  
# removes Node at the given index. returns element of the removed node.
# Check validity of index. return None if index is invalid.
    
removed_element = h7.remove(0) # This should return: 10
unittest.output_test(removed_element, '10')
print('------------------------------')
returned_value = h7.traverseList() # This should return: 20 30 40 50 60 70
unittest.output_test(returned_value, '20 30 40 50 60 70')
print('------------------------------')
removed_element = h7.remove(3) # This should return: 50
unittest.output_test(removed_element, '50')
print('------------------------------')
returned_value = h7.traverseList() # This should return: 20 30 40 60 70 
unittest.output_test(returned_value, '20 30 40 60 70')
print('------------------------------')
removed_element = h7.remove(4) # This should return: 70
unittest.output_test(removed_element, '70')
print('------------------------------')
returned_value = h7.traverseList() # This should return: 20 30 40 60 
unittest.output_test(returned_value, '20 30 40 60')
    
    
print("////// Test 11 //////")
a8 = [10,20,30,40]
h8 = LinkedList(a8) # uses theconstructor where a is an built in list
returned_value = h8.traverseList() # This should return: 10 20 30 40  
unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')    
# Rotates the list to the left by 1 position.
h8.rotateLeft()
returned_value = h8.traverseList() # This should return: 20 30 40 10  
unittest.output_test(returned_value, '20 30 40 10')
      
print("////// Test 12 //////")
a9 = [10,20,30,40]
h9 = LinkedList(a9) # uses the constructor where a is an built in list
returned_value = h9.traverseList() # This should return: 10 20 30 40
unittest.output_test(returned_value, '10 20 30 40')  
print('------------------------------')    
# Rotates the list to the right by 1 position.
h9.rotateRight()
returned_value = h9.traverseList() # This should return: 40 10 20 30
unittest.output_test(returned_value, '40 10 20 30')