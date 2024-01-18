import queue

file = open('input3_1.txt','r')
output=open('output3_1.txt','w')
n,m = map(int,file.readline().split(' '))
lst = file.readlines()

# visited=[False]*(n+1)

def create_graph(lst,n):
    graph={}

    for i in range(1,n+1):
        graph[i]=[]
    for i in lst:
        u,v=map(int,i.split(' '))
        graph[u].append(v)
    return graph


# def dfs(graph,node):
#     global visited
#     output.write(f'{node} ')
#     visited[node]=True
#     for u in graph[node]:
#         if visited[u]==False:
#             dfs(graph,u)

def bfs(graph,node):
    q=queue.Queue()
    visited=[False]*(n+1)
    q.put(node)
    while q.empty()!=True:
        u=q.get()
        if u in graph.keys():
            for v in graph[u]:
                if visited[v]==False:
                    visited[v]=True
                    q.put(v)


graph=create_graph(lst,n)
print(graph)
# dfs(graph, 1)
bfs(graph,1)
