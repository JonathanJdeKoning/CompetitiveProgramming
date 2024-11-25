ans = 0
mx = 100
ans = 0
from math import floor, ceil
for i in range(2, ceil(mx**0.5)+1):
    sq = i**2
    for j in range(sq, mx+1, sq):
        ans += sq


print(ans%1000000007)