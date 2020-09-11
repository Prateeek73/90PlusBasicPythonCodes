import re
result=[]
for password in input("Enter comma seperated passwords: ").split(','):
    if len(password)<6 or len(password)>12:
        continue
    else:
        if not re.search("[a-z]",password):
            continue
        elif not re.search("[0-9]",password):
            continue
        elif not re.search("[A-Z]",password):
            continue
        elif not re.search("[$#@]",password):
            continue
        elif re.search("\s",password):
            continue
        else:
            pass
    result.append(password)
print(','.join(result))
