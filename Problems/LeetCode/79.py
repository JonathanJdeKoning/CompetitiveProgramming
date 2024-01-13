class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word): return True

            if r not in range(rows) or c not in range(cols) or (r,c) in path or word[i] != board[r][c]:
                return False
            path.add((r,c))

            res = dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1)
            path.remove((r,c))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False
