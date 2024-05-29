mat = []
n = int(input())
for _ in range(n):
    mat.append(list(map(int, input().split())))

one = 0
two = 0
for i in range(n):
    one += mat[i][i]
    two += mat[i][(n-i)-1]
print(abs(one-two))
