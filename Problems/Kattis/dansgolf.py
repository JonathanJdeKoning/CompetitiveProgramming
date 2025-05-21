R, C, N = list(map(int, input().replace(","," ").split()))
ans = 0
diags = set()
for _ in range(N):
    x, y = list(map(int, input().replace(","," ").split()))
    mn = min(x,y)
    diags.add((x-mn, y-mn))
print(len(diags))




