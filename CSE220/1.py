def shiftLeft(source,k):
    for i in range(k):
        for i in range(len(source)-1):
            source[i]=source[i+1]
            source[i+1]=None
    return source

source=[10,20,30,40,50,60]
print(shiftLeft([10,20,30,40,50,60],3))