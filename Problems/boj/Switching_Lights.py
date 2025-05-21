N, M = list(map(int, input().replace(","," ").split()))

stalls = [0]*(N+1)

for _ in range(M):
    op, i, j =list(map(int, input().replace(","," ").split()))
    if op == 0:
        for k in range(i, j+1):
            stalls[k] = abs(stalls[k]-1)
    else:
        print(sum(stalls[i:j+1]))