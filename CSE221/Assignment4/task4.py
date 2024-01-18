file= open('input4_5.txt','r')
output=open('output4_5.txt','w')
n,m =map(int, file.readline().split(' '))
lst =file.readlines()


def graphfunc(lst,n):
    graph = {}
    for i in range(1,n+1):
        graph[i] =[]
    for k in lst:
        u,v = map(int, k.split(' '))
        graph[u].append(v)
    return graph


def checkcycle(graph, node, flag, stack):
    if stack[node] == True:
        return True
    if flag[node] == True:
        return False
    flag[node] = True
    stack[node] = True
    for c in graph[node]:
        print(c)
        if (checkcycle(graph,c, flag, stack)==True):
            print(True)
            return True
        print(False)
    stack[node] = False
    return False

def cycle(graph,n,m):
    flag = [False] *(n+1)
    print(flag)
    stack = [False] *(n+1)
    for i in range(1,n+1):
        print(i)
        if checkcycle(graph,i, flag, stack) == True: #1
            return True
    return False

graph=graphfunc(lst,n)
check = cycle(graph,n,m)
print(graph)
if check == True:
    output.write('Yes')
else:
    output.write('No')

file.close()
output.close()