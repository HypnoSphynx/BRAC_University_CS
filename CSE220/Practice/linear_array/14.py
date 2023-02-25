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

def baalercode(array,n):
    count=1
    new_array=sort(array,n)
    for i in range(len(new_array)-1):
        if new_array[i]+1==new_array[i+1]:
            count+=1
        else:
            if count>(n-count):
                break
            else:
                count=0
    print (count)
baalercode([2,6,1,9,4,5,3],7)