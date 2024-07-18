
from collections import deque

numCoins, goal = map(int, input().split())
seen = set()
coins = set([int(input()) for _ in range(numCoins)])

steps = -1
q = deque([0])

while q:
    steps += 1
    for _ in range(len(q)):
        curr = q.popleft()
        if curr==goal: print(steps);exit(0)
        if curr in seen or curr > goal: continue
        seen.add(curr)

        for coin in coins:
            if coin + curr not in seen:
                q.append(coin+curr)

print(-1)

