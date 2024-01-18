file = open('input3_1.txt')
output = open('output3_1.txt','w')
n, k = map(int, file.readline().split(' '))

parent = [i for i in range(n+1)]
node = [1 for i in range(n+1)]


def findParent(parent, r):
    if parent[r] == r:
        return r
    return findParent(parent, parent[r])

def union(parent,a,b):
    u = findParent(parent,a)
    v = findParent(parent,b)
    if u != v:
        parent[u]=v
        node[v]+=node[u]
    output.write(str(node[v])+'\n')
        
        
for i in range(k):
    n1, n2 = map(int, file.readline().split(' '))
    union(parent,n1,n2)
        
file.close()
output.close()  