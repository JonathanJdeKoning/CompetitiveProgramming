n = int(input())
shifts = [0]*1001
guards = []
for _ in range(n):
    start, end = map(int, input().split())
    guards.append((start, end))
    

    for i in range(start, end):
        shifts[i] += 1
mx = -1
base = len([x for x in shifts if x])
for s,e in guards:
    ree = base
    for i in range(s,e):
        if shifts[i] == 1:
            ree -= 1
    mx = max(mx, ree)
print(mx)
