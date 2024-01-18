from collections import defaultdict ,deque

file=open('input1_A.txt','r')
output=open('output1_A.txt','w')
n,m=map(int,file.readline().split())
lst=file.readlines()
order=""

def create_graph(lst,n):
    graph={}
    for i in range(1,n+1):
        graph[i]=[]
    for i in lst:
        u,v=map(int,i.split(' '))
        graph[u].append(v)
    return graph

# print(create_graph(lst,n))

def topological_sort_bfs(graph):
    in_degree=defaultdict(int)
    print(in_degree)
    for u in graph:
        for v in graph[u]:
            in_degree[v]+=1
    queue=deque()
    for u in graph:
        if in_degree[u]==0:
            print(in_degree[u])
            print(u)
            queue.append(u)
    
    output_array=[]

    while len(queue)!=0:
        u=queue.popleft()
        output_array.append(u)
        for v in graph[u]:
            in_degree[v]-=1
            if in_degree[v]==0:
                queue.append(v)
    return output_array


visited=[]
result=[]

def topological_sort_dfs(graph):
    global visited
    global result
    copy_graph=graph.copy() 
    for u in copy_graph.keys():
        if u not in visited:
            dfs(u)
    return result[::-1]

def dfs(u):
    global visited
    global result
    visited.append(u)
    for v in graph[u]:
        if v not in visited:
            dfs(v)
        elif v in visited and v not in result:
            return []
    result.append(u)



graph=create_graph(lst,n)
sor=topological_sort_bfs(graph)
# print(sor)