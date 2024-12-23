import random

def create_population(array):
    population=[]
    n=int(array[0].split()[0])
    t=int(array[0].split()[1])    
    for i in range(20):
        chromosome=[]
        for j in range(0,n*t):
            chromosome.append(random.randint(0,1))
        if chromosome not in population:
            population.append(chromosome)

    return population

def selection(population,n,t):

    fitness=[]
    selected=[]

    for child in range(len(population)):
        index=0 
        overlap_penalty=0
        consistency_flag=[False]*n
        consistency_penalty=0

        for j in range(t): 
            overlap_flag=False
            for k in range(n):

                if population[child][index]==1: ##overlap check
                    if overlap_flag!=True:
                        overlap_flag=True
                    else:
                        overlap_penalty+=1

                if population[child][index]==1 and consistency_flag[k]==False: ## consistency check
                    consistency_flag[k]=True
                elif population[child][index]==1 and consistency_flag[k]==True: 
                    consistency_penalty+=1

                index+=1

        for idx in range(n):
            if consistency_flag[idx]==False: # adding penalty as the course is not scheduled exactly once
                consistency_penalty+=1


        fitness_eq= -(overlap_penalty+consistency_penalty)
        fitness.append((fitness_eq,child))

    fitness.sort(key=lambda x: x[0], reverse=True)
    for i in range(len(population)//2):
        selected.append(population[fitness[i][1]])


    return selected,fitness[0][0]


def mutation(child1, child2):

    mutate_idx1=random.randint(0,len(child1)-1)
    if child1[mutate_idx1]== 1:
        child1[mutate_idx1]=0
    else:
        child1[mutate_idx1]=1

    mutate_idx2=random.randint(0,len(child2)-1)
    if child2[mutate_idx2]== 1:
        child2[mutate_idx2]=0
    else:
        child2[mutate_idx2]=1

    return child1, child2

def crossover(parent1, parent2):
    idx=random.randint(0,len(parent1)-3)
    child1=parent1[:idx]+parent2[idx:]  
    child2=parent2[:idx]+parent1[idx:]
    return child1, child2


##TASK2 
def two_point_crossover(initial_population):

    parent_idx1=random.randint(0,len(initial_population)-1)
    parent_idx2=random.randint(0,len(initial_population)-1)

    parent1=initial_population[parent_idx1]
    parent2=initial_population[parent_idx2]

    idx1=random.randint(0,len(parent1)-1)
    idx2=random.randint(idx1,len(parent1)-1)

    child1=parent1[:idx1+1]+parent2[idx1+1:idx2]+parent1[idx2:]
    child2=parent2[:idx1+1]+parent1[idx1+1:idx2]+parent2[idx2:]
    
    print(f'Offspring 1 {"".join(map(str,child1))}')
    print(f'Offspring 2 {"".join(map(str,child2))}')


def genetic_algorithm(input_arr):

    n=int(input_arr[0].split()[0])
    t=int(input_arr[0].split()[1])

    population=create_population(input_arr)
    
    ini_population_copy=population.copy()
    new_population=[]

    for iteration in range(50):
        for i in range(len(population)):
            parent1= random.randint(0,len(population)-1)
            parent2=random.randint(0,len(population)-1)

            child1, child2= crossover(population[parent1],population[parent2])
            m_child1, m_child2=mutation(child1, child2)

            new_population.append(m_child1)
            new_population.append(m_child2)

        best_childs, fitness=selection(new_population,n,t)
        population=best_childs
        new_population=[]


    output="".join(map(str,population[0]))

    print("=========================================TASK1=========================================")

    print(output)
    print(fitness)

    ###TASK2###
    print("=========================================TASK2=========================================")
    two_point_crossover(ini_population_copy)




t_n=input("")
input_arr=[t_n]
for i in range(int(t_n.split()[0])):
    input_arr.append(input())

genetic_algorithm(input_arr)




