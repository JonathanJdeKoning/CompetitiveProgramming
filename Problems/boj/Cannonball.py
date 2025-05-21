N, S = list(map(int, input().replace(","," ").split()))
S -= 1
vx = 1
A =[]
for _ in range(N):
    tar, v = list(map(int, input().replace(","," ").split()))
    A.append((tar, v))

targs = set()
seen = set()
while True:
    tar, v = A[S]
    if tar:
        if abs(vx) >= v:
            targs.add(S)
    else:
        sign = 2*int(vx < 0)-1
        vx = sign*(abs(vx) +v)
    if (S, vx) in seen: exit(print(len(targs)))
    
    seen.add((S, vx))


    S += vx

    if S < 0 or S >= N:
        exit(print(len(targs))) 