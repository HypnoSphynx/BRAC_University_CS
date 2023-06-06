f=open('input1b.txt', 'r')


for i in range(int(f.readline())):
    n=f.readline()
    int_one=''
    int_two=''
    operator=''
    flag=False
    sum=0
    for j in n:
        if j>='0' and j<='9' and flag is False:
            int_one+=j
        if j>='0' and j<='9' and flag is True:
            int_two+=j
        if j in '+-/*':
            flag=True
            operator=j
    
    
    if operator=='+':
        sum=int(int_one)+int(int_two)
    elif operator=='-':
        sum=int(int_one)-int(int_two)
    elif operator=='*':
        sum=int(int_one)*int(int_two)
    elif operator=='/':
        sum=int(int_one)/int(int_two)
    with open('output1b.txt','a') as output:
        output.write(f'The result of {int_one} {operator} {int_two} is {sum}\n')

f.close()
