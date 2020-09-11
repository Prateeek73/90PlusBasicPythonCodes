import re
lines = input()
pattern=re.compile(r'(\d+)\W')
print(re.findall(pattern,lines))