n, k = map(int, input().split())

bal = abs(sum(map(int, input().split())))
from math import ceil, floor
print(ceil(bal/k))


