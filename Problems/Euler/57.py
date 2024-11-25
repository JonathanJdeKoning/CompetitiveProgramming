from functools import cache

@cache
def f(n):
    if n ==1: return 1
    if n == 2: return 3
    return 2*f(n-1) + f(n-2)

curr = 2
num = 0
ans = 0
for i in range(2,1002):
    curr += num
    num = f(i)

    if len(str(num)) > len(str(curr)): ans += 1

print(ans)