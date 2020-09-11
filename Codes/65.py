def f(n):
    if(n==0 or n==1):
        return n
    else:
        return f(n-1)+f(n-2)
n=int(input("Enter N: "))
values = [str(f(x)) for x in range(0, n+1)]
print(", ".join(values))
