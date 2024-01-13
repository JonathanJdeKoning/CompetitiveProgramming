class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        isles = 0
        for i, row in enumerate(grid):
            for j, pos in enumerate(row):
                if pos == "1" and (i, j) not in seen:
                    isles += 1
                    q = deque([(i, j)])
                    while q:
                        curr = q.popleft()
                        y= curr[0]
                        x = curr[1]
                        if curr in seen: continue
                        seen.add(curr)

                        u = (y-1, x)
                        d = (y+1, x)
                        r = (y, x+1)
                        l = (y, x-1)

                        if u not in seen and u[0] > -1 and grid[u[0]][u[1]] == "1": 
                            q.append(u)
                        if d not in seen and d[0] < len(grid)and grid[d[0]][d[1]] == "1": 
                            q.append(d)
                        if r not in seen and r[1] < len(row) and grid[r[0]][r[1]] == "1": 
                            q.append(r)
                        if l not in seen and l[1] > -1 and grid[l[0]][l[1]] == "1": 
                            q.append(l)
        return isles
