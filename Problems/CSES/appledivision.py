from math import inf
N = int(input())
A = list(map(int, input().replace(","," ").split()))
base = sum(A)
best = inf
dfs = [(0, 0)]

while dfs:
    cum, i = dfs.pop()
    diff = abs(cum - (base-cum))
    best = min(best, diff)
    if i == len(A): continue
    poss = A[i]

    dfs.append((cum+poss, i+1))
    dfs.append((cum, i+1))
print(best)
