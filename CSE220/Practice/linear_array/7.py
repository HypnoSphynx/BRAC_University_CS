def water(array,length):
    unit=array[0]
    sum=0
    if array[1]>unit:
            return('No water will be trapped')
    else:
        for i in range(1,len(array)-1):
            if array[i]==0:
                sum+=unit
            else:
                sum+=(unit-array[i])
    return sum

print(water([3,0,0,2,0,4],6))