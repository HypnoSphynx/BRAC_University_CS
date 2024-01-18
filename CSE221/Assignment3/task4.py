def partition(array,start,end):
    pivot=array[end]
    i=start-1
    for j in range(start, end):
        if array[j]<=pivot:
            i=i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[end] =array[end],array[i+1]
    return i+1
  

def kth_smallest(array,start,end,k):
    if start <= end:
        part = partition(array,start,end)
        if part==k-1:
            return array[part]
        elif part>k-1:
            return kth_smallest(array,start,part-1,k)
        elif part<k-1: 
            return kth_smallest(array,part+1,end,k)

file=open('input4.txt','r')
output=open('output4.txt','w')
n=int(file.readline())
arr=list(map(int,file.readline().split(' ')))
for i in range(int(file.readline())): output.write(f'{kth_smallest(arr,0,n-1,int(file.readline()))}\n')
file.close()
output.close()


