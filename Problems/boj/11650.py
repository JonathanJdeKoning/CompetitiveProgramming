out = []
for _ in range(int(input())):
    out.append(tuple(map(int, input().split())))

out.sort()
for a, b in out:
    print(a,b)
