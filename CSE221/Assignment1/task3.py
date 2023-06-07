f=open('input3.txt','r')

students=int(f.readline())
id=list(map(int,f.readline().split(' ')))
marks=list(map(int,f.readline().split(' ')))
print(marks)
