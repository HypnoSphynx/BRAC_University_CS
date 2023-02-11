import math
def mean(source):
    sum=0
    for i in source:
        sum+=i
    return sum/len(source)

def sample_standard(source):
    standard_sum=0
    for i in source:
        standard_sum+=(i-mean(source))**2
    return (standard_sum/(len(source)-1))**0.5


def away(source,score):
    standard_value=sample_standard(source)
    standard_dev=mean(source)+(score*standard_value)
    print(standard_dev)
    count=0
    flag=0
    for i in source:
        if i>0 and i>standard_dev:
                count+=1
        elif i<0 and i>-standard_dev:
                count+=1
    new_array=[None]*count
    for i in range(len(source)):
        if source[i]>0 and source[i]>standard_dev and flag<=count:
                new_array[flag]=source[i]
                flag+=1
        elif source[i]<0 and source[i]>(-standard_dev) and flag<=count:
                new_array[flag]=source[i]
                flag+=1

    return new_array

print(mean([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]))
            
print(sample_standard([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]))
    

print(away([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4],1.5))
    

    

