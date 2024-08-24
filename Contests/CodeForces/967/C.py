import sys
from functools import cache

def solve():
    n = int(input())
    out = set()
    left = list(range(2, n+1))

    @cache
    def dfs(start, end):
        print(f"? {start} {end}")
        sys.stdout.flush()

        ans = int(input())

        if ans != start:
            dfs(start, ans)
            dfs(ans, end)
        else:
            out.add((min(start, end), max(start, end)))

 
    while left:
        curr = left.pop()
        dfs(1, curr)
        if len(out) == n-1:
            break
    fin = []
    for s, e in out:
        fin.append(s)
        fin.append(e)

    return f"! {' '.join(map(str, fin))}"
    

for _ in range(int(input())):
    print(solve())
    sys.stdout.flush()
