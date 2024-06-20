from functools import cache
@cache
def p(n):
    if n==0: return 1
    if n < 3: return 0
    return p(n-2) + p(n-3)

for _ in range(int(input())):
    print(p(int(input())+4))

