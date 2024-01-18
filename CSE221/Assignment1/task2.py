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


file=open('input2.txt','r')
output=open('output2.txt','w')

size=int(file.readline())
arr=list(map(float,file.readline().split(' ')))
up_arr=bubbleSort([2, 5, 1.2, 6.7, 1.7, 9.3, 2.2, 7.7, 0, -4, -5.1, 2, 5, 5.2],14)

for i in up_arr:
    output.write(str(i)+' ')

file.close()
output.close()

#Explanation: I have initiated a swap variable to check if there is any swapping happened during the first check. if the swapping is zero, this means the array is already sorted.
#Therefore if a sorted array is given, the swap variable will remain 0, thus breaking the outer loop. in this case the loop will run for n-times thus obtaining a time complexity of θ(n)