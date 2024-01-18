from collections import defaultdict

def dfs(graph,u,visited, stack):
    visited[u]=True
    for v in graph[u]:
        if visited[v]==False:
            dfs(graph,v,visited,stack)
    stack.append(u)

def transpose_graph(lst,n):
    graph={}

    for i in range(1,n+1):
        graph[i]=[]
    for i in lst:
        u,v=map(int,i.split(' '))
        graph[v].append(u)
    return graph

def main_graph(lst,n):
    graph={}

    for i in range(1,n+1):
        graph[i]=[]
    for i in lst:
        u,v=map(int,i.split(' '))
        graph[u].append(v)
    return graph

def find_strongly(graph,n,lst):
    visited=[False]*(n+1)
    stack=[]
    copy_graph=graph.copy()
    for u in copy_graph:
        if visited[u]==False:
            dfs(graph,u,visited,stack)
    transposed=transpose_graph(lst,n)
    visited=[False]*(n+1)
    components=[]

    while stack:
        u=stack.pop()
        if visited[u]==False:
            component=[]
            dfs(transposed,u,visited,component)
            components.append(component)
    return components

file=open('input3.txt','r')
n,m=map(int,file.readline().split())
lst=file.readlines()
graph=main_graph(lst,n)

print(graph)
s=find_strongly(graph,n,lst)
print(s)