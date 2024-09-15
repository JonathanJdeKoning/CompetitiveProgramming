n = int(input())
stew = sorted(map(int, input().split()))
ans = 0
for i in range(1, len(stew)-1):
    if stew[0] < stew[i] < stew[-1]:
        ans += 1

print(ans)
