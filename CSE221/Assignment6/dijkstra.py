import math
def dijkstra(graph,source,n):
    distance=[math.inf]*(n+1)
    distance[source]=0
    queue=[source]
    visited=[False]*(n+1)
    visited[source]=True

    while queue:
        u=dequeue(queue,distance,visited)
        if u in graph.keys():
            for x in graph[u]:
                v,w=x[0],x[1]
                if visited[v]==False:
                    queue.append(v)
                    temp=distance[u]+w
                    if temp<distance[v]:
                        distance[v]=temp
        if False not in visited:
            break
    distance = distance[1:]
    for i in range(len(distance)):
        if distance[i] == math.inf:
            distance[i] = -1
        output.write(str(distance[i]) + ' ')
    return
    


def dequeue(queue,distance,visited):
    min=math.inf
    for i in range(len(queue)):
        if distance[queue[i]]<min:
            idx=i
            min=distance[queue[i]]
    u=queue.pop(idx)
    visited[u]=True
    return u

file= open('input1_1.txt','r')
output = open('output1_1.txt',  'w')
n,e  = map(int, file.readline().split(' '))
l1 = file.readlines()
graph={}

for x in l1:
    if len(x) == 1:
        s = int(x)
    else:
        u,v,w=map(int, x.split(' '))
        if u in graph.keys():
            graph[u].append((v,w))
        else:
            graph[u] = [(v,w)]
dijkstra(graph,s,n)   

file.close()
output.close()



    