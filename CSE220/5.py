def shiftLeft(source,size,idx):

    for i in range(idx,size):
        source[i]=source[i+1]
    source[size-1]=0
    print(source)
        

source=[10,20,30,40,50,0,0]
shiftLeft(source,5,2)