N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
prev = mat[0]

for i in range(1, N):
    prev = [mat[i][k] + max([prev[j] for j in range(3) if j != k]) for k in range(3)]
print(prev)