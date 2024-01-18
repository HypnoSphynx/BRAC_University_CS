file=open('input2_1.txt')
output=open('output2_1.txt','w')
t,p=(map(int,file.readline().split(' ')))
array=[]

for i in range(t):
    array.append(list(map(int,file.readline().split(' '))))

assigned=[0]*(p)

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
bubbleSort(array)

final_array=[]
count=0
for i in range(len(array)):
    for j in range(len(assigned)):
        if array[i][0]>=assigned[j]:
            assigned[j]=array[i][1]
            count+=1
            break
    
output.write(str(count))
file.close()
output.close()  