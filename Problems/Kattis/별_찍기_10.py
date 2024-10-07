base = [
    ["*", "*", "*"],
    ["*", " ", "*"],
    ["*", "*", "*"]
]

def quilt(mat):
    N = len(mat)
    mat*=3
    for i, row in enumerate(mat[:N]):
        mat[i].extend(row*2)
    for i, row in enumerate(mat[N:2*N], start = N):
        mat[i].extend([" "]*N)
    #for i,row in enumerate(mat[2*N:], start = 2*N):
    #    mat[i].extend(row*2)

    return mat

for row in quilt(base):
    print("".join(row))

