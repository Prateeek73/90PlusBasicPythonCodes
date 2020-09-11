ans=list()
for i in input("Enter comma seperated list: ").split(','):
    try:
        if int(i,2)%5==0:
            ans.append(i)
    except:
        print("Invalid value found. Skipping..................")
print(",".join(ans))
