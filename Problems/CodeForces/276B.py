from collections import Counter
s = input()

fq = Counter(s)
vals = list(fq.values())
ev = 0
od = 0
for v in vals:
    if v%2==0:
        ev += 1
    else:
        od += 1
if od == 0:
    print("First")
else:
    if od%2==1:
        print("First")
    else:
        print("Second")
