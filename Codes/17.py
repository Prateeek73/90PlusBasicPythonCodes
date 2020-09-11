netAmount=0
while True:
    entry=input();
    if not entry:
        break
    else:
        parameters=entry.split()
        operation=parameters[0]
        amount=parameters[1]
        if operation=='D':
            netAmount+=int(amount)
        elif operation=="W":
            netAmount-=int(amount)
        else:
            print("Inavalid. Skipping.................")
print(netAmount)
