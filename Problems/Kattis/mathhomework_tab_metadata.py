a,b,c,n = map(int, input().split())

if a == 1 and b == 1 and c == 1:
    for i in range(n+1):
        comp = n - i

        for j in range(comp+1):
            print(i, j, comp-j)
    exit()

ans = set()
seen = set()
def dfs(x,y,z):
    if (x,y,z) in seen: return
    seen.add((x,y,z))

    curr = x*a + y*b + z*c

    if curr > n: return
    if curr == n:
        ans.add((x,y,z))
        return
    dfs(x+1,y,z)
    dfs(x,y+1,z)
    dfs(x,y,z+1)

dfs(0,0,0)
ans = sorted(ans)
if not ans:
    print("impossible")
else:
    for x in ans:
        print(" ".join(map(str, x)))