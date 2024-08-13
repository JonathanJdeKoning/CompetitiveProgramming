from functools import cache
@cache
def reach(s,e):
    if s > e: return False
    if s == e: return True

    return reach(s*10, e) or reach(s*20, e)
    

for _ in range(int(input())):
    e = int(input())
    if reach(1,e):
        print("YES")
    else:
        print("NO")
