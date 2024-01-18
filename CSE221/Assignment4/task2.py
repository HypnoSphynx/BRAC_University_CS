import queue
def create_graph(lst,n):
    graph={}

    for i in range(1,n+1):
        graph[i]=[]
    for j in lst:
        u,v=map(int,j.split(' '))
        graph[u].append(v)
        
    return graph

def bfs(graph,node):
    q = queue.Queue()
    visited = [False] * (n+1)
    q.put(node)
    while q.empty()!=True:
        u = q.get()
        output.write(f'{u} ')
        if u in graph.keys():
            for c in graph[u]:
                if visited[c] == False:
                    visited[c] = True
                    q.put(c)

file = open('input2_2.txt','r')
output=open('output2_2.txt','w')
n,m =map(int, file.readline().split(' '))
lst = list(file.readlines())
graph = create_graph(lst,n)
print(graph)
bfs(graph,1)


