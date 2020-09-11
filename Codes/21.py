import math
x=0
y=0
while True:
    entry=input()
    if entry:
        operation,value=entry.split()
        if operation=="UP":
            x+=int(value)
        elif operation=="DOWN":
            x-=int(value)
        elif operation=="RIGHT":
            y+=int(value)
        elif operation=="LEFT":
            y-=int(value)
        else:
            pass
    else:
        break
print(round(math.sqrt(x**2+y**2)))