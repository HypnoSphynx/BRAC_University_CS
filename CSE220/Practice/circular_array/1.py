def cir(arr,start,size):
    arr=arr
    idx=(start+(size))%len(arr)
    
    for i in range(size):
        print(arr[idx])
        # idx=(idx+1)%len(arr)
        idx=((start+(size-1)))%len(arr)
        size-=1
        
        # print(idx)
        
        # print(arr[idx])
        
cir([40,50,60,80,90,None,9,2,1,2,3],6,10)