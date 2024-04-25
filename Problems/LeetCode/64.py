class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = []
        for _ in range(R):
            dp.append([inf]*C)

        def get(arr,i,j, d):
            try:
                return arr[i][j]
            except IndexError:
                return d
        dp[0][0] = grid[0][0]

        
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if dp[i][j] != inf: continue
                dp[i][j] = cell + min(get(dp,i-1,j,inf),get(dp,i,j-1,inf))
        return dp[-1][-1]
