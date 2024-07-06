R, C = map(int, input().split())
mat = []
for _ in range(R):
    mat.append(list(input()))
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,-1)]
