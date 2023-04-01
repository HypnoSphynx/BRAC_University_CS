# def factorial(n):
#     if n==0:
#         return 1
#     return (n*factorial(n-1))
# print(factorial(5))

# def fibonacci(n):
#     if n==0 or n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(5))

def print_array(n,i=0):
    if i==len(n):
        return i
    print(n[i])
    print_array(n,i+1)
print_array([1,2,3,4,5])
# def base(b,n):
#     if n==1:
#         return b
#     return b*base(b,n-1)
# print(base(3,3))

