n = int(input())
a = list(map(int, input().split()))
from collections import Counter
mx = max(Counter(a).values())

if len(a) - mx >= mx-1:
    print("YES")
else:
    print("NO")
