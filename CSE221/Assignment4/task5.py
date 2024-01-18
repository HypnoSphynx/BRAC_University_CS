file = open('input5_2.txt','r')
output=open('output5_2.txt','w')
n,m,d = map(int, file.readline().split(' '))
lst = file.readlines()
q = []

def graphfunc(lst):
    graph = {}
    for k in lst:
        u,v = map(int, k.split(' '))
        if u in graph.keys():
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph.keys():
            graph[v].append(u)
        else:
            graph[v] = [u]
    return graph

graph = graphfunc(lst)
print(graph)
def bfs(graph, s, d):
    if s == d:
        return [s]
    q = [(s,[s])]
    
    while q:
        print(q)
        (u,path) = q.pop(0)
        for c in graph[u]:
            if c == d:
                path+=[c]
                return path
            else:
                q.append((c,path+[c]))
path = bfs(graph,1, d)

string=''
for x in path:
    string+=str(x)+' '

output.write(f'Time:{len(path)-1}\n')
output.write(f'Shortest Path: {string}')

file.close()
output.close()

