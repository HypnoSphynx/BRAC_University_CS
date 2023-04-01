# def pattern(n,i=0):
#     def print_val(n,i=1):
#         if i==n+1:
#             return i
#         if i==n:
#               print(i)
#         else:
#             print(i,end=' ')
#         print_val(n,i+1)

#     if i!=n:
#         print_val(i+1)
#         pattern(n,i+1)
    
# pattern(5)

def pattern(n,i=0):
    def print_val(n,i=1):
        if i==n+1:
            return i
        if i==n:
              print(i)
        else:
           
            print(i,end=' ')
        print_val(n,i+1)

    if i!=n:
        print(end='  '*(n-i))
        print_val(i+1)
        pattern(n,i+1)
    

pattern(5)