def shiftLeft(source,k):
    for i in range(k):
        for i in range(len(source)-1):
            source[i]=source[i+1]
            source[i+1]=None
    return source

def rotateLeft(source,k):
    for i in range(k):
        temp=source[0]
        source=shiftLeft(source,1)
        source[len(source)-1]=temp
    return source

source=[10,20,30,40,50,60]
print(rotateLeft(source,3))