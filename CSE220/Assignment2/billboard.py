s1=input('Enter string 1: ')
s2=input('Enter string 2: ')
def check(inp1,inp2):
    if len(inp1)>10 and len(inp2)>10:
        return True
    return False
def backwardforward(inp1,inp2,start1,start2):
    output1=''
    start1=start1
    idx1=start1
    for i in range(len(inp1)):
        output1+=inp1[idx1]
        if idx1==0:
            idx1=len(inp1)
        idx1-=1
    output2=''
    start2=start2
    idx2=start2
    for i in range(len(inp2)):
        output2+=inp2[idx2]
        idx2=(idx2+1)%len(inp2)
    return f'{output1}\n{output2}'
def billboard(inp1,inp2):
    
    start_one=None
    start_two=None
    if check(inp1,inp2)==False:
        array=[['']*len(inp1),['']*len(inp2)]  
        for i in range(len(array)):
            for j in range(len(array[i])):
                if i==0:
                    array[i][j]=inp1[j]
                    if ord(inp1[j])>=65 and ord(inp1[j])<=90 and start_one==None:
                        start_one=j
                else:
                    array[i][j]=inp2[j]
                    if ord(inp2[j])>=65 and ord(inp2[j])<=90 and start_two==None:
                        start_two=j
        print(f'Top board Start Character: {inp1[start_one]}')
        print(f'Top board Start index: {start_one}')
        print(f'Bottom board Start Character: {inp2[start_two]}')
        print(f'Bottom board Start index: {start_two}')
        print('Press any key and then press enter to continue!!!')
        run='a'
        while run!='Q' and run!='q':
                if start_one==0:
                    start_one=len(inp1)-1
                elif start_two==0:
                    start_two=len(inp2)-1
                print(backwardforward(inp1,inp2,start_one,start_two))
                start_one-=1
                start_two-=1
                run=input()
    else:
        print('Invalid Input')
billboard(s1,s2)

    



