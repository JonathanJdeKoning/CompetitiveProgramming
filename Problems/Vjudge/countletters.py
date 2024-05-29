from collections import Counter
s = input()
c = Counter(s)
for k,v in sorted(dict(c).items()):
    print(f"{k} : {v}")
