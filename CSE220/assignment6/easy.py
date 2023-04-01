def binary(n):
    if n==0:
        return n
    binary(n//2)
    print(n%2,end='')

binary(5)


class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n



def add_element(head):
    
    if head.next==None:
      return head.element
    return head.element+add_element(head.next)

three=Node(6,None)
two=Node(2, three)
head=Node(1,two)

print(add_element(head))

def backward_printing(head):
    if head.next!=None:
        backward_printing(head.next)
    print(head.element)
backward_printing(head)