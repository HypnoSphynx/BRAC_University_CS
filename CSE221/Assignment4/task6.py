file = open('input6_3.txt','r')
outputf=open('output6_3.txt','w')
row,col = map(int, file.readline().split(' '))
lst = file.readlines()
print(lst)
arr=[]
for x in lst:
    ar=[]
    for y in x:
        ar.append(y)
    if ar[-1] == '\n':
        ar = ar[:-1]
    arr.append(ar)

visited = [[False for i in range(col)] for j in range(row)]
print(visited)

def dfs(arr, visited, i,j,row, col):
    stack = []
    stack.append([i, j])
    visited[i][j] = True
    diamond = 0
    while stack!=[]:
        temp = stack.pop(len(stack)-1)
        r,c = temp[0], temp[1]
        if arr[r][c] == 'D':
            diamond+=1

        if r-1 > -1:
            if visited[r-1][c] == False and arr[r-1][c] !='#':
                stack.append([r-1,c])
                visited[r-1][c] = True

        if r+1 < row:
            if visited[r+1][c] == False and arr[r+1][c] !='#':
                stack.append([r+1,c])
                visited[r+1][c] = True

        if c-1 > -1:
            if visited[r][c-1] == False and arr[r][c-1] != '#':
                stack.append([r,c-1])
                visited[r][c-1] = True

        if c+1 < col:
            if visited[r][c+1] == False and arr[r][c+1] != '#':
                stack.append([r,c+1])
                visited[r][c+1] = True
    return diamond

output = 0
for i in range(row):
    for j in range(col):
        if visited[i][j] == False and arr[i][j] != '#':
            output = max(output, dfs(arr,visited,i,j,row,col))

outputf.write(str(output))

file.close()
outputf.close()