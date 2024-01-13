class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        isles = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in seen:
                    isles += 1
                    q = deque([(i, j)])
                    while q:
                        curr = q.popleft()
                        y, x= curr[0], curr[1]
                        if curr in seen: continue
                        seen.add(curr)

                        directions = [[0,1],[1,0],[-1,0],[0,-1]]
                        for dr, dc in directions:
                            newy, newx = y+dr, x+dc
                            if not newy in range(rows): continue
                            if not newx in range(cols):  continue

                            if (newy, newx) not in seen and grid[newy][newx] == "1":
                                q.append((newy, newx))
        return isles
