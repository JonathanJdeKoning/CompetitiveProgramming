n, q = map(int, input().split())
arrs = []
for _ in range(n):
    arrs.append([])

for _ in range(q):
    data = input().split()
    if data[0] == "1":
        print(" ".join(arrs[int(data[1])]))
    elif data[0] == "2":
        arrs[int(data[1])] = []
    else:
        arrs[int(data[1])].append(data[2])

        
