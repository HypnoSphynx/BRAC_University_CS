def shiftLeft(source,k):
    for i in range(k,len(source)-1): #made a little change in shiftLeft, it will start the loop from the given index and will start shifiting left from that
        source[i]=source[i+1]
        source[i+1]=None
    return source

def remove(source,idx):
    source[idx]=0
    source=shiftLeft(source,idx)
    return source

def removeAll(source,k):
    count=0
    while count< len(source):
        if source[count]==k:
            source=remove(source,count)
            count=0
        count+=1
    return source



source=[10,2,30,2,50,2,2,1,2,1,78,456,54,35,34,23,432,4,564,34,1,1,2,3,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,0,0]

print(removeAll(source,2))
