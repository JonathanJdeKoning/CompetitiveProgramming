N = int(input())
A = list(map(int, input().replace(","," ").split()))
a, b = list(map(int, input().replace(","," ").split()))
ans = 0

for i in range(a+1, b+1):
    ans += A[i-2]
print(ans)