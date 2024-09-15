n = int(input())
s = input()
from itertools import pairwise
if "L" not in s:
    l = s.index("R")
    r = len(s) - s[::-1].index("R")
    print(l+1,r+1)
elif "R" not in s:
    l = s.index("L")+1
    r = len(s) - s[::-1].index("L") + 1
    print(r-1,l-1)
else:
    l = s.index("R") + 1
    r = s.index("L")
    print(l,r)
