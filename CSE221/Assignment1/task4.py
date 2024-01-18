f=open('input4.txt','r')
output=open('output4.txt','w')

input_s=int(f.readline())
train=[]
for i in range(input_s):
    train.append(f.readline().strip('\n'))

for i in range(input_s):
    max_idx = i
    for j in range(i+1, input_s):
        trainA=train[max_idx].split(' ')
        trainB=train[j].split(' ')
        if trainA[0] >trainB[0]:
            max_idx = j
        elif trainA[0] ==trainB[0]:
            if trainA[len(trainA)-1] ==trainB[len(trainB)-1]:
                pass
            elif (trainA)[len(trainA)-1] <trainB[len(trainB)-1]:
                max_idx = j
    temp=train[i]
    train[i]=train[max_idx]
    train[max_idx]=temp


for i in range(input_s):
    output.write(f'{train[i]}\n')

output.close()
f.close()