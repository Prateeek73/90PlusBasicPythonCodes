from operator import itemgetter, attrgetter
l = []
while True:
    params = input()
    if not params:
        break
    l.append(tuple(params.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))
