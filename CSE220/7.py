def splitting_array(source):
    sum=0
    sum2=0
    for i in range(len(source)):
        sum+=source[i]
        for j in range(i+1,len(source)):
            sum2+=source[j]
        if sum==sum2:
            return True
        else:
            if i==len(source)-1:
                return False
            else:
                sum2=0
        
        


print(splitting_array( [2, 1, 1, 2, 1]))