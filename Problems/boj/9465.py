for _ in range(int(input())):
    n = int(input())
    mat = []
    for _ in range(2):
        mat.append(list(map(int, input().split())))
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = mat[0][0]
    dp[1][0] = mat[1][0]
    try:
        dp[0][1] = mat[0][1] + mat[1][0]
        dp[1][1] = mat[1][1] + mat[0][0]
    except: pass
    for i in range(2,n):
        topval = mat[0][i]
        dp [0][i] = max(topval+dp[1][i-1], topval+dp[0][i-2], topval+dp[1][i-2])
        botval = mat[1][i]
        dp [1][i] = max(botval+dp[0][i-1], botval+dp[0][i-2], botval+dp[1][i-2])
    print(max(max(dp[0]), max(dp[1])))
