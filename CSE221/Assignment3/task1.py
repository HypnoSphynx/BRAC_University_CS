def merge(a, b,z):
    merged= []
    i,j = 0,0
    count=z
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            merged += [b[j]]
            j += 1
            count+=len(a)-i 
        else:
            merged += [a[i]]
            i += 1
    merged += a[i::]
    merged += b[j::]
    return merged,count

def alienCount(arr,count=0):
    if len(arr)==1:
        return arr,0
    mid=len(arr)//2
    x,c1=alienCount(arr[:mid])
    y,c2=alienCount(arr[mid:])
    return merge(x,y,c1+c2)


file=open('input1.txt','r')
output=open('output1.txt','w')
size=int(file.readline())
array=list(map(int,file.readline().split(' ')))
output.write(f'{alienCount(array)[1]}')
file.close()
output.close()