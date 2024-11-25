
N,K = list(map(int, input().split()))
A = [int(input()) for _ in range(N)]
l = 0
r = K
mx = sum(A[l:r])
curr = mx
while r < len(A):
    curr -= A[l]
    l += 1
    curr += A[r]
    r += 1

    mx = max(mx, curr)
print(mx)

