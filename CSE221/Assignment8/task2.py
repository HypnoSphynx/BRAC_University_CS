file=open('input2_4.txt')
output=open('output2_4.txt','w')

n=int(file.readline())

array=[None]*(n+1)

def steps(n):
    global array
    if n==1 or n==0:
        return n
    elif n==2:
        return 2
    elif array[n]==None:
        array[n]=steps(n-1)+steps(n-2)
    return array[n]
output.write(str(steps(n)))

file.close()
output.close()