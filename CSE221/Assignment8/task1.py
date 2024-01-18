import math

def dijkstra(graph, source, n):
    c = 0
    distance = [math.inf] * (n + 1)
    distance[source] = 0
    queue = [source]
    visited = [False] * (n + 1)
    visited[source] = True

    while queue:
        u = dequeue(queue, distance, visited)
        if u in graph.keys():
            for x in graph[u]:
                v, w = x[0], x[1]
                if visited[v] == False and w < distance[v]:
                    queue.append(v)
                    distance[v] = w
                    c += w
        if False not in visited:
            break

    return c

def dequeue(queue, distance, visited):
    min_dist = math.inf
    idx = -1
    for i in range(len(queue)):
        if distance[queue[i]] < min_dist:
            idx = i
            min_dist = distance[queue[i]]
    u = queue.pop(idx)
    visited[u] = True
    return u

file= open('input1_2.txt','r')
output = open('output1_2.txt',  'w')
n,e  = map(int, file.readline().split(' '))
l1 = file.readlines()
graph={}


for i in range(1,n+1):
    graph[i]=[]
for x in l1:
    u,v,w=map(int, x.split(' '))
    if u in graph.keys():
        graph[u].append((v,w))
    if v in graph.keys():
        graph[v].append((u,w))

c = dijkstra(graph, 1, n)

output.write(str(c))