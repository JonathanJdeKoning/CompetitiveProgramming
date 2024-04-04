from collections import deque
n = int(input())
runners = {}
best = []

for _ in range(n):
    runner, first, rest = input().split()
    first = float(first)
    rest = float(rest)
    runners[runner] = (first, rest)
fastest = deque(sorted(runners.items(), key = lambda x:x[1][1],reverse=True))
print(fastest)
total = sum([x[1][1] for x in fastest[1:4]]) + fastest[0][1][0]




