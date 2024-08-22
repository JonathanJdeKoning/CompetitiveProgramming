R, C, n = map(int, input().split())

mat = [["."]*C for _ in range(R)]

for _ in range(n):
    y,x = map(int, input().split())
    mat[y-1][x-1] = "*"

for row in mat:
    print("".join(row))

