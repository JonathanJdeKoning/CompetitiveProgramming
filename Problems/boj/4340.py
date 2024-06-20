from collections import deque
import copy
goby = int(input())
for loop in range(goby):
    R,C,n = map(int, input().split())
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    mat =[list(input()) for _ in range(R)]
    for _ in range(n):
        new = copy.deepcopy(mat)
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                for dy, dx in directions:
                    y = i+dy
                    x = j+dx
                    if min(y,x) == -1 or y==R or x==C: continue
                    if cell == "R" and mat[y][x] == "P":
                        new[i][j] = "P";break
                    elif cell == "P" and mat[y][x] == "S":
                        new[i][j] = "S";break
                    elif cell == "S" and mat[y][x] == "R":
                        new[i][j] = "R";break
                else:
                    new[i][j] = cell
        mat = copy.deepcopy(new)
    for row in mat:
        print("".join(row))
    if loop != goby-1:
        print()
                    
