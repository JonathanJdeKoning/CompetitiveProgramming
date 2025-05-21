from copy import copy
N = 3
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

while zeros:
    i,j = zeros.popleft()

    poss = copy(nums)
    poss -= get_box(i,j)
    poss -= get_row(i,j)
    poss -= get_col(i,j)
    if len(poss) == 1:
        mat[i][j] = poss.pop()
        continue
    
