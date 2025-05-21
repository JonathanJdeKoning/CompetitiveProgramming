N = int(input())
for _ in range(N):
    data = input().split()
    op = data[0]
    if op == "INNTAK":
        name = data[1]
        out = data[2]