d={'UPPERCASE':0,
   'LOWERCASE':0}
for c in input("Enter the sentence"):
    if c.isupper():
        d["UPPERCASE"]+=1
    elif c.islower():
        d["LOWERCASE"]+=1
    else:
        pass
for key,value in d.items():
    print(key+" : "+str(value))
