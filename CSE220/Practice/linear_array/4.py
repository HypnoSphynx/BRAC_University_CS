def freq_check(array,n,x):
    count=0
    for i in range(n):
        if array[i]==x:
            count+=1
    
    return count
print(freq_check([1,1,1,1,1],5,1))