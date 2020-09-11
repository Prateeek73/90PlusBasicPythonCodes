def f(n):
    if(n==0):
        return 1
    else:
        return f(n-1)+100
n=int(input("Enter N: "))
if(n>0):
    print(f(n))