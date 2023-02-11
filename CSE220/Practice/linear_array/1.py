nm=input('enter size')
sum=0
for i in range(len(nm)):
    if nm[i]!=' ':
     sum+=int(nm[i])
str1=input('enter str1')
str2=input('enter str2')

def find_union(sum,str1,str2):
    array=[None]*sum
    count=0
    for i in range(len(str1)):
        if str1[i]!=' ' and str1[i] not in array:
            array[count]=str1[i]
            count+=1
    
    for i in range(len(str2)):
        if str1[i]!=' ' and str1[i] not in array:
            array[count]=str2[i]
            count+=1
    return count
print(find_union(sum,str1,str2))
