
f=open('input1a.txt','r')

string=''
for i in range(int(f.readline())):
    n=int(f.readline())
    if n%2==0:
        string=str(n)+' is an even number\n'
    else:
        string=str(n)+' is an odd number\n'
    
    with open('output1a.txt', 'a') as output:
        output.write(string)
f.close()

    

    

