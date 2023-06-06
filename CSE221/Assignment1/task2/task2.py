def bubbleSort(arr,size):
    for i in range(size-1):
        swap_flag=0
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag+=1
        if swap_flag==0:
            break
    return arr

f=open('input2.txt','r')

arr=[]

size=int(f.readline())
string=f.readline()
elem=''

for j in string:
    if j==' ':
        arr.append(int(elem))
        elem=''
    else:
        elem+=j
if elem!=' ':
    arr.append(int(elem))


up_arr=bubbleSort(arr,size)


for i in up_arr:
    with open('output2.txt','a') as output:
        output.write(str(i)+' ')

