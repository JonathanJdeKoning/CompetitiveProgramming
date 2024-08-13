def solve():
    n,s,m = map(int, input().split())
    tasks = []
    for _ in range(n):
        start,end = map(int, input().split())
        tasks.append((start,end))

    tasks.sort()

    curr = 0
    for start, end in tasks:
        time = start - curr
        if time >= s: return "YES"
        curr = end
    time = m - curr
    if time >= s: return"YES"
    return "NO"
for _ in range(int(input())):
    print(solve())
