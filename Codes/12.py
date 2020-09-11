values=list()
for i in range(2000,3001,2):
    s=str(i)
    if (int(s[1])%2==0) and (int(s[2])%2==0):
        values.append(s)
print(",".join(values))
