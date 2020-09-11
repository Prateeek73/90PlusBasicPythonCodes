import re
emailAddress = input()
pattern=re.compile(r'(\w+)@(\w+)\.(\w+)')
groups = re.match(pattern,emailAddress)
print(groups.group(2))