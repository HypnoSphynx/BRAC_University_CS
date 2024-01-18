

file = open('input1.txt','r')
output = open('output1.2.txt','w')

data=list(map(str,file.readline().split(' ')))
n=int(data[0])
s=int(data[1])
array=list(map(str,file.readline().split(' ')))

dic={}
for i in range(n):
    dic[array[i]] = str(i+1)
flag = False

for i in range(n):
    m = s - int(array[i])
    if str(m) in array:
        output.write(dic[array[i]]+' '+ dic[str(m)])
        flag = True
        break
if flag == False:
    output.write('IMPOSSIBLE')
