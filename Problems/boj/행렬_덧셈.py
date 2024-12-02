R, C = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(R)]
B = [list(map(int, input().split())) for _ in range(R)]
for i in range(R):
    for j in range(R):
        B[i][j] += A[i][j]

print("\n".join([" ".join(map(str, row)) for row in B]))
        