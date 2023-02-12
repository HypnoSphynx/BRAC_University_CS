def sort(array):
    count=0
    while count<=len(array):
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
        count+=1
    return array

def smallest(array,n,k):
    array=sort(array)
    print(array)
    return array[k-1]

print(smallest( [7, 10, 4, 3, 20, 15],6,3))
print(smallest( [7, 10, 4, 20, 15],5,4))