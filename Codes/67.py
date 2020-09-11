def NumGenerator(n):
    i=0
    while i<=n:
        if i%5==0 and i%7==0:
            yield i
        i+=1

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))
print(", ".join(values))
