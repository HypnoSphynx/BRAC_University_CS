def r_max(a,b):
    if a>b:
        return a
    else:
        return b

def find_max(arr):
    if len(arr)==1:
        return arr
    else:
        mid=len(arr)//2
        a1=find_max(arr[mid:])
        a2=find_max(arr[:mid])
        return r_max(a1,a2)
file=open('input4.txt','r')
output=open('output4.txt','w')
n=int(file.readline())
array=list(map(int,file.readline().split(' ')))
output.write(f'{find_max(array)[0]}')
file.close()
output.close()

#Time complexity of this code is O(nlogn)