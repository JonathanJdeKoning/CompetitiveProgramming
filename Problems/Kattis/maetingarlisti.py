n, R, C = map(int, input().split())
mat = [input().split() for _ in range(R)]

for i in range(R):
    row = []
    for j in range(C):
        row.append(input())
    if row == mat[i]:
        print("left")
    else:
        print("right")
