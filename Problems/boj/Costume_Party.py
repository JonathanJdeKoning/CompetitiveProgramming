N, K = list(map(int, input().split()))
ans = 0
A = sorted([int(input()) for _ in range(N)])
for i in range(len(A)-1):
    val = A[i]
    low = i+1
    high = len(A)

    while low < high:
        mid = (low + high) // 2

        if A[mid] + val > K:
            high = mid
        else:
            low = mid + 1
    low -= 1 
    if val + A[low] <= K:
        ans += low - i
print(ans)
    
