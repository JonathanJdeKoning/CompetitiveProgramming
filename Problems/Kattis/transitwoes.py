leave, start, routes = list(map(int, input().split()))
walktime = list(map(int, input().split()))
ridetime = list(map(int, input().split()))
arrive = list(map(int, input().split()))

for idx,walk in enumerate(walktime):
    leave += walk
    try:
        while leave % arrive[idx] != 0:
            leave += 1
        leave += ridetime[idx]
    except IndexError: pass
if leave <= start:
    print("yes")
else:
    print("no")
