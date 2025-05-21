from itertools import permutations
order = sorted(['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue'])
req = []
for _ in range(int(input())):
    data = input().split()
    a, b = data[0], data[-1]
    req.append((a,b))
for p in permutations(order):
    idx = {cow: i for i, cow in enumerate(p)}
    for a, b in req:
        if abs(idx[a] - idx[b]) != 1:
            break
    else:
        exit(print("\n".join(p)))