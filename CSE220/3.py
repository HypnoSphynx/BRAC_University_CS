def shiftLeft(source,k):

    new_array=[0]*len(source)

    for i in range(k): 
        new_array[k]=source[i]
        k+=1  
    print(new_array)

source=[10,20,30,40,50,60]
shiftLeft(source,3)