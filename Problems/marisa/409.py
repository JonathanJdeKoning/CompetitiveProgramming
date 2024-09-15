N = int(input())
A = list(map(int, input().split()))

mx = A[-1]
ans = 0
for n in A[::-1][1:]:
    if n > mx:
        mx = n
        ans += 1

print(ans)
