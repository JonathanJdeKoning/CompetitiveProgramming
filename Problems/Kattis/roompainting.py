nSizes, nMicro = map(int, input().split())
def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
sizes = sorted([int(input()) for _ in range(nSizes)])
from bisect import bisect_left, bisect_right

total = 0

for _ in range(nMicro):
    q = int(input())
    total += find_ge(sizes, q) - q
print(total)
