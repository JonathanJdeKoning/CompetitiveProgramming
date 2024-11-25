for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) < 3:
        print(f"Data Set {tc+1}:")
        print(max(A))
        print()
        continue
    dp = [0]*len(A)
    dp[0] = A[0]
    dp[1] = max(A[1], A[0])
    for i in range(2, len(A)):
        dp[i] = max(dp[i-1], A[i] + dp[i-2])
    print(f"Data Set {tc+1}:")
    print(dp[-1])
    print()