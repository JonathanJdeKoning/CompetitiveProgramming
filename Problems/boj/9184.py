from functools import cache
@cache
def w(a,b,c):
    if min(a,b,c) <=0: return 1
    if max(a,b,c)> 20: return w(20,20,20)
    return w(a-1,b,c) + w(a-1,b-1,c)+ w(a-1,b,c-1) - w(a-1,b-1,c-1)

while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1: break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
