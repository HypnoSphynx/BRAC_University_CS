class Node:
    def __init__(self,elem):
        self.elem=elem
        self.left=None
        self.right=None

def tree(arr,i,n):
    root=None
    if i<n:
        if arr[i]!=None:
            root=Node(arr[i])
            root.left=tree(arr,2*i,n)
            root.right=tree(arr,2*i+1,n)
    return root

def pre_order(root):
    if root!=None:
        print(root.elem,end='')
        pre_order(root.left)
        pre_order(root.right)

def in_order(root):
    if root!=None:
        in_order(root.left)
        print(root.elem,end=' ')
        in_order(root.right)

def post_order(root):
    if root!=None:
        post_order(root.left)
        post_order(root.right)
        print(root.elem,end='')

def get_height(root):
    if root==None:
        return -1
    else:
        return 1+max(get_height(root.left),get_height(root.right))
         
def get_level(root):
    if root==None:
        return 0
    else:
        return 1+get_level(root.left)+get_level(root.right)

array=[None,'a','b','c','d','e','f','g','h',None,None,None,'i','j',None,'k']
root=tree(array,1,len(array))      

print(get_height(root))

array1=[None]*((get_height(root)+1))**2

def array_cons(root,i):
    if root==None:
        return None
    else:
        array1[i]=root.elem
        array_cons(root.left,2*i)
        array_cons(root.right, 2*i+1)

array_cons(root,1)
print(array1) 