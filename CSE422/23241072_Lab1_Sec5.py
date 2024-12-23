import math

def generate_graph(lst):
    graph={}
    heuristic={}
    for lines in lst:
        nodes=lines.split(' ')
        temp=[]



        for i in range(0,len(nodes)-1,2):
            temp.append([nodes[i],nodes[i+1]]) 
        

        heuristic[temp[0][0]]= int(temp[0][1]) #Generating heuristic dictionary

        for i in range(len(temp)-1): #Generating graph

            if temp[0][0] in graph.keys():
                graph[temp[0][0]].append((temp[i+1][0],int(temp[i+1][1])))
            else:
                graph[temp[0][0]]=[(temp[i+1][0],int(temp[i+1][1]))]

    


    return graph,heuristic

def frng(queue):
    minimum = math.inf
    for i in range(len(queue)):
        if queue[i][1] <minimum:
            idx = i
            minimum = queue[idx][1]
    node = queue.pop(idx)
    return node

def generate_path(parent,source,goal):

    path=[]
    node=goal
    output=""

    for i in range(len(parent)):
        path.append(node)
        if node not in parent.keys():
            break
        node=parent[node]
        if node==source:
            path.append(node)
            break

    if node!=source:
        return "NO path found"

    for i in range(len(path)):
        if i==0:
            output=path[i]
        else:
            output= path[i]+"--->"+output

    return output


def astar(lst,source,goal):

    graph,heuristic=generate_graph(lst)

    if goal not in heuristic.keys():
        print("Path not found")
        return
    
    distance ={}
    for i in graph.keys():
        distance[i]=math.inf
    distance[source]=0



    queue= [[source,heuristic[source]]]
    visited_nodes = {"Arad": False, "Bucharest": False, "Craiova": False, "Drobeta": False, "Eforie": False, "Fagaras": False, 
               "Giurgiu": False, "Hirsova": False, "Iasi": False, "Lugoj": False, "Mehadia": False, "Neamt": False, "Oradea": False, 
               "Pitesti": False, "Rimnicu": False, "Sibiu": False, "Timisoara": False, "Urziceni": False, "Vaslui": False, "Zerind": False}
    parent={}


    while queue:
        visiting, visit_cost, = frng(queue) 

        if graph[visiting]== False:
            continue 

        visited_nodes[visiting] = True

        if visiting == goal:
            break

        if visiting in graph.keys():

            for iterating in graph[visiting]: #iterating current node's members
                

                v, w = iterating[0] , iterating[1]
                temp_cost=distance[visiting]+w

                if temp_cost< distance[v]:
                    distance[v]=temp_cost
                    cost=temp_cost+heuristic[v]
                    queue.append([v,cost])
                    parent[v]=visiting

    output=generate_path(parent,source,goal)

    print(f'Path: {output}')
    print(f"Total distance: {distance[goal]} km")



file=open("input.txt","r")
lst=file.readlines()

source= input("Start node: ")
destination= input("Destination: ")
# source="Arad"
# destination="Bucharest"
astar(lst,source,destination)

file.close()

