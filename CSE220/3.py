def shiftRight(source,k): 
    for i in range(k):
        for i in range(len(source)-1,0,-1):
            source[i]=source[i-1]
        source[0]=None
    return source

source=shiftRight([10,20,30,40,50,60],3)
print(source)