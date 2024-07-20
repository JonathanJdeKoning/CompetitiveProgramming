n, k = map(int, input().split())
from collections import Counter

count = Counter([int(input()) for _ in range(n)])

mx = max(count.values())

if n - mx <= k: print("Ja")
else:
    print("Nej")

