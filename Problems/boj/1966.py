from collections import deque
for _ in range(int(input())):
    n,m = map(int, input().split())
    printer = deque(list(map(lambda x: [int(x), False], input().split())))
    printer[m][1] = True
    minutes = 0

    while True:
        prio, mine= printer.popleft()
        if not printer: print(minutes+1);break
        if max([x[0] for x in printer]) > prio: printer.append((prio, mine));continue
        minutes += 1
        if mine: print(minutes);break





