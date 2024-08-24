n,k = map(int, input().split())


for i in range(n):
    row = [0]*n
    row[i] = k
    print(" ".join(map(str, row)))

