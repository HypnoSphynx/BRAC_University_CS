def left(array,start,size,steps):
    arr=array
    arr1=[None]*len(array)
    idx=((start+(size-1)))%len(array)
    idx2=((start+(size)))%len(array)
    for i in range(len(arr1)):
        arr1[i]=arr[i]
    for i in range(steps):
        arr=arr1
        for i in range(size+1):
            
            arr1[idx2]=arr[idx]
            idx=((start+(size-1)))%len(arr)
            idx2=((start+(size-2)))%len(arr)
            size-=1
    print(arr1)
    
left([2,5,6,7,4],3,5,2)