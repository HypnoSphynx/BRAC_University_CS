from collections import defaultdict ,deque


def topological_sort_bfs(graph):
    in_degree= defaultdict(int)

    for u in graph:
        for v in graph[u]:
            in_degree[v]+=1
    queue=deque()

    for u in graph:
        print(u)
        if in_degree[u]==0:
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


file=open('input1_A.txt','r')
output=open('output1_A.txt','w')
n,m=map(int,file.readline().split())
graph=defaultdict(list)
order=""

for i in range(m):
    u,v=map(int,file.readline().split())
    graph[u].append(v)

sorted_output=topological_sort_bfs(graph)


if len(sorted_output)!=n:
    order='Impossible'
else:
    for i in sorted_output:
        order+=str(i)+' '
print(graph)


output.write(order)
file.close()
output.close()


