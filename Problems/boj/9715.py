for _ in range(int(input())):
    R, C = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(list(map(int, input())))
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    total = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val != 0:
                total += 2
            for dy,dx in directions:
                y = i+dy
                x = j+dx
                if x==-1 or y ==-1 or x==C or y==R:
                    total += val
                    continue
                else:
                    total += max(val-grid[y][x],0)
    print(total)
