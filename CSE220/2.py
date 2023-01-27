def shiftLeft(source,k):

    new_array=[0]*len(source)

    for i in range(0,len(source)-k): 
        new_array[i]=source[k]
        new_array[k]=source[i]
        k+=1  
    print(new_array)

source=[10,20,30,40,50,60]
shiftLeft(source,3)