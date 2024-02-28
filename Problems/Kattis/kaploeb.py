numtimes, needed , numnums = map(int, input().split())
parts = {}

for i in range(numtimes):
    num, time = map(float, input().split())
    num = int(num)

    if num not in parts:
        parts[num] = [0,0]
    parts[num][0] += 1
    parts[num][1] += time

good = sorted([(k,round(v[1],2)) for k, v in parts.items() if v[0] >= needed], key=lambda x: (x[1],x[0]))
debug(good,"good")
