inputLine=input("Enter the line:").split(" ")
inputLine=list(dict.fromkeys(inputLine))
print(" ".join(sorted(inputLine)))
