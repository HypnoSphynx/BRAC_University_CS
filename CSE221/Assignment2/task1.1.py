def find_sum(array,s):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==s:
                return i+1,j+1
file=open('input1.txt','r')
output=open('output1.1.txt.','w')

data=list(map(int,file.readline().split(' ')))
array=list(map(int,file.readline().split(' ')))
index=find_sum(array,data[1])

output.write(f'{index[0]} {index[1]}')
file.close()
output.close()