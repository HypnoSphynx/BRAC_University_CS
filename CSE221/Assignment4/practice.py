#file_read
import queue

file=open('input2_2.txt','r')
n,e=map(int,file.readline().split(' '))
lst=file.readlines()

def create_graph(lst,n):

    graph={}
    for i in range(1,n+1):
        graph[i]=[]
    for i in lst:
        u,v=map(int,i.split(' '))
        graph[u].append(v)
    return graph

visited=[False]*(n+1)

def dfs(graph,node):
    global visited
    visited[node]==True
    print(node)
    for u in graph[node]:
        if visited[u]==False:
            dfs(graph,u)

def bfs(graph,node):
    visited=[False]*(n+1)
    q=queue.Queue()
    q.put(node)
    while q.empty()!=True:
        u=q.get()
        print(u)
        if u in graph.keys():
            for v in graph[u]:
                if visited[u]==False:
                    visited[v]=True
                    q.put(v)

print(create_graph(lst,n))

flag=[False]*(n+1)
parent_tracker=[False]*(n+1)

def detect_cycle(graph,n):
    global flag
    global parent_tracker
    
    for i in range(1,n+1):
        if checkcycle(graph,i)==True:
            return True
        return False
def checkcycle(graph,node):
    if parent_tracker[node]==True:
        return True
    if flag[node]==True:
        return False
    parent_tracker[node]=True
    flag[node]=True
    for u in graph[node]:
        if checkcycle(graph,u)==True:
            return True
    parent_tracker[node]=False
    return False
