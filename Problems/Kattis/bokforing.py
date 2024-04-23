numpeople, numqueries = map(int, input().split())

d = {}
curr = 0
for _ in range(numqueries):
    data = input().split()

    if data[0] == "SET":
        d[data[1]] = int(data[2])
    elif data[0] == "RESTART":
        curr = int(data[1])
        d = {}
    elif data[0] == "PRINT":
        print(d.get(data[1], curr))


