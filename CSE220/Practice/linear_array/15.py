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
def merge(array1,array2):
    new_array=[None]*(len(array1)+len(array2))
    count=0
    for i in range(0,len(array1)):
        new_array[count]=array1[i]
        count+=1
    for i in range(len(array2)):
        new_array[count]=array2[i]
    new_array=sort(new_array)
    odd_count=None
    even_count=None
    if len(new_array)%2!=0:
        odd_count=(len(new_array))//2
    else:
        odd_count=(len(new_array)+1)//2
        even_count=(len(new_array)-1)//2
    if even_count==None:
        median=new_array[odd_count]
    else:
        median=(new_array[odd_count]+new_array[even_count])/2
    return median
print(merge([1,3],[2]))