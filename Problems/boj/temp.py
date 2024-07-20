
import itertools
import copy
from collections import deque

def spread_virus(lab_map, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    virus_map = copy.deepcopy(lab_map)
    queue = deque()

    for i in range(n):
        for j in range(m):
            if virus_map[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and virus_map[nx][ny] == 0:
                virus_map[nx][ny] = 2
                queue.append((nx, ny))

    return virus_map

def get_safe_area(lab_map, n, m):
    safe_area = 0
    for i in range(n):
        for j in range(m):
            if lab_map[i][j] == 0:
                safe_area += 1
    return safe_area

def main():
    n, m = map(int, input().split())
    lab_map = []
    for _ in range(n):
        lab_map.append(list(map(int, input().split())))

    empty_spaces = [(i, j) for i in range(n) for j in range(m) if lab_map[i][j] == 0]
    wall_combinations = itertools.combinations(empty_spaces, 3)
    
    max_safe_area = 0
    
    for walls in wall_combinations:
        temp_map = copy.deepcopy(lab_map)
        for x, y in walls:
            temp_map[x][y] = 1
        virus_spread_map = spread_virus(temp_map, n, m)
        safe_area = get_safe_area(virus_spread_map, n, m)
        max_safe_area = max(max_safe_area, safe_area)
    
    print(max_safe_area)

if __name__ == "__main__":
    main()
