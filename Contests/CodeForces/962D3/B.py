for _ in range(int(input())):
    n, k = map(int, input().split())
    mat = []
    for _ in range(n):
        mat.append(list(input()))

    new = []

    for i in range(0, n, k):
        row = []
        for j in range(0,n,k):
            row.append(mat[i][j])
        new.append(row)
    

    for row in new:
        print("".join(row))




