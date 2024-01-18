file=open('input1_1.txt')
output=open('output1_1.txt','w')
array=[]

for i in range(int(file.readline())):
    array.append(list(map(int,file.readline().split(' '))))


def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
bubbleSort(array)

end=0
final_array=[]

for i in range(len(array)):
    if array[i][0]>=end:
        end=array[i][1]
        final_array.append(array[i])

output.write(str(len(final_array))+'\n')
for i in range(len(final_array)):
    output.write(f'{final_array[i][0]} {final_array[i][1]}\n')
    


file.close()
output.close()  