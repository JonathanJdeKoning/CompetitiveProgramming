n,m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(" ".join(input().split()[::-1]))
for row in mat:
    print(row)
