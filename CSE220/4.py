def shiftRight(source,k): 
    for i in range(k):
        for i in range(len(source)-1,0,-1):
            source[i]=source[i-1]
        source[0]=None
    return source

def rotateRight(source,k):
    for i in range(k):
        temp=source[len(source)-1]
        source=shiftRight(source,1)
        source[0]=temp
    return source
source=[10,20,30,40,50,60]
print(rotateRight(source,3))