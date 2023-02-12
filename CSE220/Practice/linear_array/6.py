def sort(array,n):
    count=0
    while count<=n:
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
        count+=1
    return array
print(sort([0, 2, 1, 2, 0],5))