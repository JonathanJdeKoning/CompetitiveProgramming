s = input()
t = input()
from collections import Counter
if Counter(s) != Counter(t):
    exit(print("NO"))
if len(s) != len(t): exit(print("NO"))
bad = 0
for a,b in zip(s,t):
    if a!= b:
        bad += 1
if bad ==0 or bad ==2:
    print("YES")
else:
    print("NO")
