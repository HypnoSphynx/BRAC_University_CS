#method-1
import time
def remove(source,idx):
    for i in range(idx,len(source)):
        if i==len(source)-1: #condition for setting last element as 0
            source[i]=None
            break
        else:
            source[i]=source[i+1] #shifting left
    return source
#method 2
def shiftLeft(source,k):
    for i in range(k,len(source)-1): #made a little change in shiftLeft, it will start the loop from the given index and will start shifiting left from that
        source[i]=source[i+1]
        source[i+1]=None
    return source

def remove(source,idx):
    source[idx]=0
    source=shiftLeft(source,idx)
    return source
        

source=[10,20,30,40,50,0,0]
remove(source,2)
print(source)

