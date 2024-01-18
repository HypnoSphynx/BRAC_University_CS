def merge(a, b):
    merged= []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged += [a[i]]
            i += 1
        else:
            merged += [b[j]]
            j += 1
    merged += a[i::]
    merged += b[j::]
    return merged

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)


file=open('input3.txt','r')
output=open('output3.txt','w')
n=int(file.readline())
array=list(map(int,file.readline().split(' ')))
array=mergeSort(array,)
for i in array: output.write(f'{i} ')
file.close()
output.close()