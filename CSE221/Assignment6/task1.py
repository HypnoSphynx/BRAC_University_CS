import math
      
def dequeue(queue, distance, flag):
    minimum = math.inf
    for i in range(len(queue)):
        if distance[queue[i]] <minimum:
            idx = i
            minimum = distance[queue[idx]]
    u = queue.pop(idx)
    flag[u] = True
    return u

def dijkstra(graph,s,n):
    distance = [math.inf] * (n+1)  
    distance[s] = 0 
    queue = [s]       
    flag = [False] * (n+1) 
    flag[s] = True         
    while queue:
        u = dequeue(queue, distance, flag)
        if u in graph.keys():
            for x in graph[u]: 
                v, w = x[0] , x[1]
                if flag[v] == False:   
                    # queue.append(v)
                    print(queue)
                    temp = distance[u] + w
                    
                    if temp < distance[v]:
                        
                        distance[v] = temp
                        queue.append(v)              
        if False not in flag:
            break
    distance = distance[1:]
    for i in range(len(distance)):
        if distance[i] == math.inf:
            distance[i] = -1
        output.write(str(distance[i]) + ' ')
    return


file= open('input.txt','r')
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