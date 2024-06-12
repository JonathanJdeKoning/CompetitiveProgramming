R,C = map(int, input().split())
mat = []

for _ in range(R):
    mat.append(list(input()))
from math import inf
mn = inf
for i in range(R-7):
    for j in range(C-7):
        diff = 0
        for k in range(8):
            rowpar =k%2
            section = mat[i+k][j:j+8]

        
            for l in range(8):
                colpar = l%2
                c = section[l]
                if (colpar+rowpar)%2==1: corr ="B"
                else: corr = "W"

                if c != corr:
                    diff += 1
        mn = min(mn, min(64-diff, diff))


print(mn)
        
        

