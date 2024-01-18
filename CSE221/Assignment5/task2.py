from collections import defaultdict ,deque


def topological_sort_bfs(graph):
    in_degree= defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v]+=1
    queue=deque()
    print(in_degree)
    for u in graph:
        if in_degree[u]==0:
            queue.append(u)
    output_array=[]

    while len(queue)!=0:
        queue=deque(sorted(queue))
        u=queue.popleft()
        output_array.append(u)
        for v in graph[u]:
            in_degree[v]-=1
            if in_degree[v]==0:
                queue.append(v)

    return output_array

file=open('input2.txt','r')
n,m=map(int,file.readline().split())
graph=defaultdict(list)
str1=""
print(graph)

for i in range(m):
    u,v=map(int,file.readline().split())
    graph[u].append(v)
print(graph)
sorted_order=topological_sort_bfs(graph)
output=open('output2.txt','w')


print(sorted_order)
if len(sorted_order)!=n:
    str1='Impossible'
else:
    for i in sorted_order:
        str1+=str(i)+' '

output.write(str1)
file.close()
output.close()

