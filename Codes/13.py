d={'DIGITS':0,
   'LETTERS':0}
for c in input("Enter the sentence"):
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
for key,value in d.items():
    print(key+" : "+str(value))
