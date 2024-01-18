def partition(array,start,end):
    pivot=array[end]
    i=start-1
    for j in range(start, end):
        if array[j]<=pivot:
            i=i+1
            array[i], array[j]=array[j], array[i]
    array[i+1], array[end]=array[end],array[i+1]
    return i+1
  

def quicksort(array, start, end):
    if start<end:
        part=partition(array,start,end)
        quicksort(array,start,part-1)
        quicksort(array,part+1,end)


file=open('input3.txt','r')
output=open('output3.txt','w')
n=int(file.readline())
arr=list(map(int,file.readline().split(' ')))
quicksort(arr,0,n-1)
for i in arr: output.write(str(i)+' ')
file.close()
output.close()