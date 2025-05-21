N = int(input())
ans = 0
while N >= 5:
    N//=5
    ans += N

print(ans)