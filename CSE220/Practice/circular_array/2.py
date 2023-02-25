def left(array,start,size):
    arr=array
    arr1=[None]*len(array)
    idx=start
    idx2=start+1
    for i in range(len(arr1)):
        arr1[i]=arr[i]
    for i in range(size):
        print(idx2)
        arr1[idx2]=arr[idx]
        idx=(idx+1)%len(arr)
        idx2=(idx2+1)%len(arr)
        
    print(arr1)
    
left([2,5,6,7,4],3,5)