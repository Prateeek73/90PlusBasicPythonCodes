from random import shuffle
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
values=[i+" "+j+" "+k for i in subjects for j in verbs for k in objects]
shuffle(values)
print("\n".join(values))