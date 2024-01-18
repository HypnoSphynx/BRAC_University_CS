import math
def dequeue(queue, distance, flag,path):
    minimum = math.inf
    for i in range(len(queue)):
        if distance[queue[i]] < minimum:
            idx = i
            minimum = distance[queue[idx]]
    u = queue.pop(idx)
    flag[u] = True
    
    return u

def dijkstra(graph,s,n):
    distance = [math.inf] * (n+1)  
    distance[s] = 0
    queue = [s]       
    path =[s]
    flag = [False] * (n+1)  
    flag[s] = True            
    
    while queue:
        u = dequeue(queue, distance, flag, path)
        if u not in path:
            path.append(u)    
        if u in graph.keys():
            for x in graph[u]: 
                v, w = x[0] , x[1]
                if flag[v] == False:   
                    queue.append(v)
                    temp = distance[u] + w
                    if temp < distance[v]:
                        distance[v] = temp
   
        if False not in flag:
            break
    return (distance,path)


file = open('input2_3.txt','r')
output = open('output2_3.txt',  'w')
n,e  = map(int, file.readline().split(' '))
l1 = file.readlines()
graph={}
for y in l1:
    x = list(map(int,y.split(' ') ))
    if len(x) ==2:
        s1,s2 = x[0],x[1]
    else:
        u,v,w=x[0],x[1],x[2]
        if u in graph.keys():
            graph[u].append((v,w))
        else:
            graph[u] = [(v,w)]


a = dijkstra(graph,s1,n)
d1, p1 = a[0], a[1]
b = dijkstra(graph,s2,n)
d2, p2 = b[0], b[1]
i,j=0,0
print(p1,d1)
print(p2,d2)
while True:
    if p1[i] == p2[j]:
        temp = p1[i]
        output.write('Time '+str(max(d1[temp],d2[temp]))+'\n')
        output.write('Node '+str(temp))
        break
    if i == len(p1)-1 and j == len(p2)-1:
        output.write('IMPOSSIBLE')
        break
    if i!=len(p1)-1: 
        i+=1
    if j!=len(p2)-1: 
        j+=1
file.close()
output.close()