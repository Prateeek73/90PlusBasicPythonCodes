import math
def getValue(int D):
    C=50
    H=30
    return str(int(round(math.sqrt((2 * C * D)/H))))

outputList=list()
for value in input("Enter: ").split(','):
    outputList.append(getValue(value))
print(','.join(outputList))
