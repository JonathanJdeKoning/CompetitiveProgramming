M, N = list(map(int, input().replace(","," ").split()))

degree = {i: [0,0] for i in range(1, M+1)}
for _ in range(N):
    u,v = list(map(int, input().replace(","," ").split()))
    degree[u][1] += 1
    degree[v][0] += 1

oneMoreIn = 0
oneMoreOut = 0 
for k in degree:
    if degree[k][0] == degree[k][1]: continue
    if degree[k][0] == degree[k][1]+1:
        if not oneMoreIn:
            oneMoreIn = k
        else:
            exit(print("no"))
    elif degree[k][0] +1 == degree[k][1]:
        if not oneMoreOut:
            oneMoreOut = k
        else:
            exit(print("no"))
    else:
        exit(print("no"))
if not oneMoreOut and not oneMoreIn:
    exit(print("anywhere"))

if oneMoreOut and oneMoreIn:
    exit(print(oneMoreOut, oneMoreIn))
print("no")