from copy import copy, deepcopy
N = int(input())
A =  [list(x) for x in input().split()]
for i, num in enumerate(A):
    for j, c in enumerate(num):
        for new in "0123456789":
            if new == c: continue
            if new == "0" and j == 0 and len(num) != 1:
                continue
            poss = deepcopy(A)
            poss[i][j] = new
            poss = [int("".join(x)) for x in poss]
            if poss != sorted(poss):
                exit(print(*poss))
print("impossible")