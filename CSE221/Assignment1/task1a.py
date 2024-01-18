file=open('input1a.txt','r')
output=open('output1a','w')
string=''
for i in range(int(file.readline())):
    n=int(file.readline())
    if n%2==0:
        string=str(n)+' is an even number\n'
    else:
        string=str(n)+' is an odd number\n'
    
    
    output.write(string)
file.close()

    

