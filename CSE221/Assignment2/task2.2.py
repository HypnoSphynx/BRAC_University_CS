file = open('input2.txt','r')
output = open('output2.2.txt','w')
nx=int(file.readline())
array1=list(map(str,file.readline().split(' ')))
mx=int(file.readline())
array2=list(map(str,file.readline().split(' ')))
array=[None]*(nx+mx)

n=0
m=0
for k in range(mx+nx):
    if n==nx:
        array=array+array2[m:]
        break
    if m==mx:
        array=array+array1[n:]
        break
    if int(array1[n])<int(array2[m]):
        array[k]=str(int(array1[n]))
        n+=1
    elif int(array1[n])>int(array2[m]):
        array[k]=str(int(array2[m]))
        m+=1

for i in array:
    if i!=None:
        output.write(i+' ')
output.close()
file.close()