from math import dist, ceil, floor
N = int(input())
ans = [None]*N
cranes = []
mp = {}
for i in range(N):
    x,y,h= list(map(int, input().replace(","," ").split()))
    cranes.append((h,x,y))
    mp[h] = i
cranes.sort()
for i, (ch,cx,cy) in enumerate(cranes):
    mxHeight = ch
    for j, (_,nx,ny) in enumerate(cranes[i+1:]):

        d = dist((cx,cy), (nx,ny))
        mxHeight = min(mxHeight, floor(d))
    ans[mp[ch]] = mxHeight

print("\n".join(map(str, ans)))