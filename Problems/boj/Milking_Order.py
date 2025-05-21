from copy import copy
N, M, K = list(map(int, input().replace(","," ").split()))
heir = list(map(int, input().replace(","," ").split()))
skip = set()
order = [0]*N

for _ in range(K):
    cow, pos = list(map(int, input().replace(","," ").split()))
    order[pos-1] = cow
if 1 in order:
    exit(print(order.index(1) + 1))
mn = len(order)-1
before = copy(heir)
after = heir
if 1 in heir:
    idx = heir.index(1)
    before = heir[:idx+1]
    after = heir[idx+1:]

while after:
    curr = after.pop()
    if curr in order:
        mn = order.index(curr)
        continue
    for i in range(mn, -1, -1):
        if order[i] == 0:
            order[i] = curr
            mn = i
            break
before = before[::-1]
mn = 0
while before:
    curr = before.pop()
    if curr in order:
        mn = order.index(curr)
        continue
    for i in range(mn, len(order)):
        if order[i] == 0:
            order[i] = curr
            mn = i
            break
if 1 in order:
    print(order.index(1)+1)
else:
    print(order.index(0) + 1)
#print(order)