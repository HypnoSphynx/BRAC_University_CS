from collections import defaultdict

def dfs(u,graph,visited,stack):
    visited[u]=True
    for v in graph[u]:
        if not visited[v]:
            dfs(v,graph,visited,stack)
    stack.append(u)

def transpose_graph(graph):
    transposed=defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)
    return transposed

def find_strongly_connected_components(graph):
    visited= defaultdict(bool)
    stack=[]
    copy_graph=graph.copy()

    for u in copy_graph:
        if not visited[u]:
            dfs(u,graph,visited,stack)
    transposed=transpose_graph(graph)
    visited= defaultdict(bool)
    components=[]

    while stack:
        u=stack.pop()
        if not visited[u]:
            component=[]
            dfs(u,transposed,visited,component)
            components.append(component)

    return components

file=open('input3.txt','r')
output=open('output3.txt','a')

n,m=map(int,file.readline().split())
graph=defaultdict(list)
str1=""

for i in range(1,n+1):
    graph[i]=[]

for i in range(m):
    u,v=map(int,file.readline().split())
    graph[u].append(v)

s=find_strongly_connected_components(graph)
print(s)
for i in s:
    s=''
    for j in range(len(i)):
        if j==len(i)-1:
            s+=str(i[j])+'\n'
        else:
            s+=str(i[j])+' '
    output.write(s)
# output.write()
file.close()
output.close()

