from itertools import pairwise
a,b,c = sorted(list(map(int, input().replace(","," ").split())))
if a == b-1 and b == c-1:
    exit(print("0\n0"))

mn = None
mx = None

diffs = [b-a, c-b]
if 2 in diffs:
    mn = 1
else:
    mn = 2

mx = max(diffs) - 1
print(mn)
print(mx)
