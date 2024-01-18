from collections import defaultdict

def topological_sort_dfs(graph):
    def dfs(u):
        visited.add(u)
        print(visited)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
            elif v in visited and v not in result:
                return []
        result.append(u)
    visited=set()
    result=[]
    print(visited)
    
    copy_graph=graph.copy()
    for u in copy_graph.keys():
        if u not in visited:
            dfs(u)
    return result [::-1]


file=open('input1_A.txt','r')
output=open('output1_A.txt','w')
n,m=map(int,file.readline().split())
graph=defaultdict(list)
order=""

for i in range(m):
    u,v=map(int,file.readline().split())
    graph[u].append(v)

sorted_output=topological_sort_dfs(graph)
print(sorted_output)

if len(sorted_output)!=n:
    order='Impossible'
else:
    for i in sorted_output:
        order+=str(i)+' '


output.write(order)
file.close()
output.close()
