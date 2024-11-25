N = int(input())
best = []
bestdiff = 9999999999999999
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            if i*j*k == N:
                diff = 2*(i*j + j*k + k*i)
                if diff < bestdiff:
                    bestdiff = diff
                    best = [i,j,k]
if not best:
    print(1,1,N)
else:
    print(*best) 
