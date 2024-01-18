import numpy as np
file=open('input1a_2.txt','r')
output=open('output1a_2.txt','w')
n, v = tuple(map(int,file.readline().split(" ")))
adj_mat=np.array([[0]*(n+1)]*(n+1))


for i in range(v):
    u,v,w=tuple(map(int,file.readline().split(' ')))
    adj_mat[u][v]=w


for i in adj_mat:
    string=''
    for j in i:
        string+=str(j)+(' ')
    output.write(f'{string}\n')
    string=''









