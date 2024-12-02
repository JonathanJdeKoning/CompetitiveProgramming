from collections import defaultdict
from math import inf
while True:
    try:
        N,M = list(map(int, input().split()))
    except EOFError: break
    mat = [list(map(int, input().split())) for _ in range(N)]
    ans = (0,0)
    best = inf
    bestsub = None 
    subs = 0
    for i in range((N-M)+1):
        for j in range((N-M)+1):
            subs += 1
            fq = set()
            submat = [row[j:j+M] for row in mat[i:i+M]]
            for row in submat:
                for num in row:
                    fq.add(num)
            if len(fq) < best:
                best = len(fq)
                ans = (i+1,j+1)
                bestsub = fq
            elif len(fq) == best:
                for a,b in zip(sorted(list(bestsub)), sorted(list(fq))):
                    if a!= b:
                        if b > a:
                            bestsub = fq
                            ans = (i+1, j+1)
                            break
                        else: break
        

    print(*ans)
                

