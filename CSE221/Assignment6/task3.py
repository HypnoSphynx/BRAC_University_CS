import math

file = open('input3_1.txt','r')
output = open('output3_1.txt',  'w')
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


distance = [math.inf] * (n+1)
distance[1] = 0
flag = [False] * (n+1)
flag[0] = True


for k in range(n):
    minimum = math.inf
    minimum_node = None
    
    for j in range(1,n+1):
        if flag[j] == False and distance[j] < minimum:
            minimum = distance[j]
            minimum_node = j
    if minimum_node == None: 
        if any(flag) == True:
            output.write('IMPOSSIBLE')
        break
    if minimum_node == n :
        output.write(str(minimum))
        break
    flag[minimum_node] = True
    if minimum_node in graph.keys():
        for x in graph[minimum_node]:
            v,w = x[0], x[1]
            d = max(minimum, w)
            if d<distance[v]:
                distance[v] = d
if minimum_node != n:
    if False in flag:
        output.write('IMPOSSIBLE')
file.close()
output.close()