file=open('input1a_2.txt','r')
output=open('output1b_2.txt','w')
n, m = tuple(map(int,file.readline().split(" ")))
adj_mat = [[]for j in range(n+1)]


for i in range(m):
    u,v,w=tuple(map(int,file.readline().split(' ')))

    adj_mat[u].append((v,w))


for i in range(len(adj_mat)):
    string=f'{i}: '
    for j in range(len(adj_mat[i])):
        string+=str(adj_mat[i][j])+(' ')
    output.write(f'{string}\n')
    string=''
