output=[i for i in input("Enter the list: ").split(',') if int(i)%2!=0]
print(','.join(output))
