g = [list(map(int, input().split())) for _ in range(5)]

from itertools import permutations
perms = list(permutations([1,2,3,4,5]))



mx = 0
def happ(p):
    a,b,c,d,e = p
    a-=1
    b-=1
    c-=1
    d-=1
    e-=1
    ans = 0

    ans += g[a][b] + g[b][a] + g[c][d]+ g[d][c]
    ans += g[b][c] + g[c][b] + g[d][e] + g[e][d]
    ans += g[c][d] + g[d][c]
    ans += g[d][e] + g[e][d]
    return ans
for perm in perms:
    mx = max(mx, happ(perm))

print(mx)

