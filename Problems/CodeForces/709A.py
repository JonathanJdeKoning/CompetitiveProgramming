n,b,d = map(int, input().split())

a = list(map(int, input().split()))
waste = 0
ans = 0
for o in a:
    if o > b: continue
    waste += o
    if waste > d:
        waste = 0
        ans += 1
print(ans)
