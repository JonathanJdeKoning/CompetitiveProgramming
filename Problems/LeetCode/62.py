class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = []
        for i in range(m):
            memo.append([0]*n)
        memo[0][0] = 1
        for i in range(m):
            for j in range(n):
                up = memo[i-1][j] if i > 0 else 0
                left = memo[i][j-1] if j > 0 else 0
                memo[i][j] += up+left
        return memo[-1][-1]
