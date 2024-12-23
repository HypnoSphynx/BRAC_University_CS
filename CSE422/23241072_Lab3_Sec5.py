print("==========================================================================TASK 01==========================================================================")

import random
max_node=True
branching_factor=2
def generate_tree():

    tree = [random.choice([-1, 1]), random.choice([-1,1]),random.choice([-1, 1]), random.choice([-1,1]),random.choice([-1, 1]), random.choice([-1,1]),random.choice([-1, 1]), random.choice([-1,1]),
            random.choice([-1, 1]), random.choice([-1,1]),random.choice([-1, 1]), random.choice([-1,1]),random.choice([-1, 1]), random.choice([-1,1]),random.choice([-1, 1]), random.choice([-1,1])]
    return tree


def alpha_beta(tree, depth, idx, alpha, beta):

    if depth==5:
        return tree[idx]
    
    global max_node, branching_factor


    if max_node: #max nodes
        node_value=float("-inf")
        for i in range(branching_factor):
            max_node=False
            temp=alpha_beta(tree, depth+1, idx*2+i, alpha, beta)
            node_value=max(node_value,temp)
            alpha=max(alpha,temp)
            if beta<=alpha:
                break
        return node_value
    else:   #min nodes
        node_value=float("inf")
        for i in range(branching_factor):
            max_node=True
            temp=alpha_beta(tree, depth+1, idx*2+i, alpha, beta)
            node_value=min(node_value,temp)
            beta=min(beta,temp)
            if beta<=alpha:
                break
        return node_value



def mortal_combat(player):
    
    if player==0:
        player= "Scorpion"
        opponent= "Sub-Zero"
    elif player==1:
        player= "Sub-Zero"
        opponent= "Scorpion"
        
    win=0
    lose=0
    round_win=[]

    for i in range(3):
        temp=alpha_beta(generate_tree(), 1,0, float("-inf"), float("inf"))
        if temp==1:
            win+=1
            round_win.append(player)
        elif temp==-1:
            lose+=1
            round_win.append(opponent)
    
    if win>lose:
        print(f"Game Winner: {player}")
    else:
        print(f"Game Winner: {opponent}")

    print("Total Rounds Played: 3")

    for i in range(len(round_win)):
        print(f'Winner of Round {i+1}: {round_win[i]}')

mortal_combat(int(input("Enter 0 for Scorpion and 1 for Sub-Zero: ")))




print("==========================================================================TASK 02==========================================================================")

max_node=True
branching_factor=2

def alpha_beta_pac_man(tree, depth, idx, alpha, beta,dark_magic,cost):

    if depth==4:
        return tree[idx]
    
    global max_node, branching_factor


    if max_node: #max nodes

        node_value=float("-inf")
        
        for i in range(branching_factor):
            max_node=False
            temp=alpha_beta_pac_man(tree, depth+1, idx*2+i, alpha, beta,dark_magic,cost)
            node_value=max(node_value,temp)
            alpha=max(alpha,temp)
            if beta<=alpha:
                break

        return node_value
    elif max_node==False and dark_magic==True: #dark magic nodes

        node_value=float("-inf")
        
        for i in range(branching_factor):
            max_node=True
            temp=alpha_beta_pac_man(tree, depth+1, idx*2+i, alpha, beta,dark_magic,cost)
            node_value=max(node_value,temp)
            alpha=max(alpha,temp)
            if beta<=alpha:
                break

        return node_value-cost
    else:   #min nodes
        node_value=float("inf")

        for i in range(branching_factor):
            max_node=True
            temp=alpha_beta_pac_man(tree, depth+1, idx*2+i, alpha, beta,dark_magic,cost)
            node_value=min(node_value,temp)
            beta=min(beta,temp)
            if beta<=alpha:
                break

        return node_value
    

def pac_man(cost):
    tree = [3,6,2,3,7,1,2,0]
    dark_magic_used= alpha_beta_pac_man(tree, 1,0, float("-inf"), float("inf"),True,cost)
    global max_node
    max_node=True
    dark_magic_not_used= alpha_beta_pac_man(tree, 1,0, float("-inf"), float("inf"),False,0)

    if dark_magic_used>dark_magic_not_used:
        print(f"The new minimax temp is {dark_magic_used}. Pacman goes right and uses dark magic")
    else:
        print(f"The new minimax temp is {dark_magic_not_used}. Pacman does not use dark magic")


pac_man(int(input("Enter Dark Magic Cost: ")))
    