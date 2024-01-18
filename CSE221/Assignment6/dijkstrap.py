import math
file= open('input1_1.txt','r')
output = open('output1_1.txt',  'w')
n,e  = map(int, file.readline().split(' '))
lst = file.readlines()
graph={}
s=None
for i in range(len(lst)):
    if i==len(lst)-1:
        s=int(lst[i])
    else:
        u,v,w=map(int(i.split(' ')))
        if u not in graph.keys():
            graph[u]=[(v,w)]
        else:
            graph[u].append((v,w))

def djikstra(graph,source,n):
    distance=[math.inf]*(n+1)
    distance[source]=0
    queue=[source]
    visited=[False]*(n+1)
    visited[source]=True

    while queue:
        u=deque(graph,distance)
        visited[u]=True
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
        distance=distance[1::]
        return distance

    
def deque(queue,distance):
    min=math.inf
    for i in range(len(queue)):
        if distance[queue[i]]<min:
            min=distance[queue[i]]
            idx=i
    u=queue.pop(idx)
    return u