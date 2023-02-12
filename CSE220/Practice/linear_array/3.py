def arr(arry,n,s):
    array=arry
    length=n
    element=s
    position_one=0
    position_two=0
    count=0
    while True:
        sum=0
        for i in range(count,length):
            sum+=array[i]
            if sum==element:
                return f'{count+1} {i+1} {sum}'
        count+=1

print(arr([1,2,3,4,5,6,7,8,9,10],10,15))
print(arr([1,2,3,7,5],5,12))