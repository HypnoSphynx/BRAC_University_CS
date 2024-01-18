f=open('input3.txt','r')
output=open('output3.txt','w')

students=int(f.readline())
id=list(map(int,f.readline().split(' ')))
marks=list(map(int,f.readline().split(' ')))

for i in range(students):
    swap=0
    max_idx = i
    for j in range(i+1, students):
        if marks[max_idx] < marks[j]:
            max_idx = j
        elif marks[max_idx]==marks[j]:
            if id[j]<id[max_idx]:
                max_idx=j
                
    temp=marks[i]
    marks[i]=marks[max_idx]
    marks[max_idx]=temp

    temp=id[i]
    id[i]=id[max_idx]
    id[max_idx]=temp




for i in range(students):
    output.write(f'ID: {id[i]} Mark: {marks[i]}\n')

output.close()
f.close()
