C, R = list(map(int, input().split()))
mat = [list(input()) for _ in range(R)]
directions = [(-1,0),(1,0),(0,1),(0,-1)]
seen = set()

for i in range(R):
    for j in range(C):
        