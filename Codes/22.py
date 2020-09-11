d={}
for word in input("Input :").split():
    d[word]=d.get(word,0)+1
for key in sorted(d.keys()):
    print("{}:{}".format(key, d[key]))