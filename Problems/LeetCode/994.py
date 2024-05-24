
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions  = [(0,-1),(0,1),(-1,0),(1,0)]
        q = deque([])
        R, C = len(grid), len(grid[0])
        fresh = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 2:
                    q.append((i,j))
                elif cell == 1:
                    fresh.add((i,j))
        if not fresh: return 0
        time = -1

        while q:
            time += 1
            for _ in range(len(q)):
                y,x = q.popleft()
                for dy, dx in directions:
                    newY = y+dy
                    newX = x+dx

                    if min(newY, newX) < 0 or newY == R or newX == C or grid[newY][newX] != 1: continue
                    grid[newY][newX] = 2
                    fresh.discard((newY, newX))
                    q.append((newY, newX))
        return time if not fresh else -1
