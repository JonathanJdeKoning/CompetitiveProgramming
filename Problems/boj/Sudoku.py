from copy import copy
N = int(input())
mat = []
nums = set(range(1, N**2+1))
zeros = []
for i in range(N**2):
    row = [int(x) for x in input().split()]
    for j in range(N**2):
        if row[j] == 0: zeros.append((i,j))
    mat.append(row)

def get_box(i,j):
    y = N*(i//N)
    x = N*(j//N)
    box = []
    for z in range(N):
        box.extend(mat[y+z][x:x+N])
    return set(box)
def get_row(i,j):
    return set(mat[i])

def get_col(i,j):
    return set([row[j] for row in mat])
best = 0
def dfs(k):
    global best
    if k == len(zeros):
        exit(print("\n".join([" ".join(map(str, row)) for row in mat])))
    if k > best:
        best = k
        print(best)
    i,j = zeros[k]
    if mat[i][j] != 0:
        return

    poss = copy(nums)
    poss -= get_box(i,j)
    poss -= get_row(i,j)
    poss -= get_col(i,j)

    if not poss:
        return

    for p in poss:
        mat[i][j] = p
        dfs(k+1)
    mat[i][j] = 0 
dfs(0)