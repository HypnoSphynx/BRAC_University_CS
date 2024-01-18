
file = open('input3_1.txt','r')
output=open('output3_1.txt','w')
n,m = map(int,file.readline().split(' '))
lst = file.readlines()

visited = [False]* (n+1)

def createGraph(lst,n):
    graph = {}
    for i in range(1,n+1):
        graph[i] =[]
    for k in lst:
        u,v = map(int, k.split(' '))
        graph[u].append(v)
    return graph

def dfs(visited, graph, node):
    output.write(f'{node} ')
    visited[node] = True
    for c in graph[node]:
        if visited[c]==False:
            dfs(visited,graph,c)

graph=createGraph(lst,n)
dfs(visited, graph, 1)

file.close()
output.close()