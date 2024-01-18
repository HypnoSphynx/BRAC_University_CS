import sys
def find_ij(array,size):
    max_i=(-sys.maxsize-1,0)
    max_j=(-sys.maxsize-1,0)
    index=1
    for k in range(size-1):
        if array[k]<0:
            if abs(array[k])>=max_j[0]:
                if max_j[0]>max_i[0]:
                    max_i=max_j
                max_j=(array[k],k)
                index=k
        elif array[k]>max_j[0] or array[k]>max_i[0]:
            if array[k]>max_j[0]:
                if max_j[0]>max_i[0]:
                    max_i=max_j
                max_j=(array[k],k)
                index=k
            elif array[k]>max_i[0] and k!=index:
                max_i=(array[k],k)
    if max_i[1]>max_j[1]:
        output=max_j[0]+max_i[0]**2
    else:
        output=max_i[0]+max_j[0]**2


    return output

file=open('input2.txt','r')
output=open('output2.txt','w')
n=int(file.readline())
arr=list(map(int,file.readline().split(' ')))
output.write(f'{find_ij(arr,n)}')
file.close()
output.close()