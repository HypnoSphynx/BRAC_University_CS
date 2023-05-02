class Node:
    def __init__(self,elem):
        self.elem=elem
        self.left=None
        self.right=None

def addNode(root,i):
    if i<root.elem and root.left is  None:
        root.left=Node(i)
    elif i>root.elem and root.right is None:
        root.right=Node(i)
    if i<root.elem and root.left is not None:
        addNode(root.left,i)
    elif i>root.elem and root.right is not None:
        addNode(root.right,i)

def in_order(root):
    if root!=None:
        in_order(root.left)
        print(root.elem,end=' ')
        in_order(root.right)

l1=[70,50,40,90,20,60,20,95,99,80,85,75]
root=Node(l1[0])
for i in range(1,len(l1)):
    addNode(root,l1[i])
in_order(root)

#deletion

def minValueNode(root):
    current=root
    while current.left!=None:
        current=current.left
    return current

def delete(root,key):
    if root is None:
        return None
    if key<root.elem:
        root.left=delete(root.left,key)
    elif key>root.elem:
        root.right=delete(root.right,key)
    
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.right
            root=None
            return None
        temp=minValueNode(root.right)
        root.key=temp.elem
        root.right=delete(root.right,temp.elem)
        return root

    