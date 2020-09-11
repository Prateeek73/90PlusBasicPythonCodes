R=int(input("Enter no. of rows:"))
C=int(input("Enter no. of columns:"))
matrix=[[i*j for i in range(C)] for j in range(R)]
print(matrix)
