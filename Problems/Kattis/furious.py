numpots, time = list(map(int, input().split()))

pots = []

for _ in range(numpots):
    pots.append(int(input()))

    pots = sorted(pots, reverse=True)
print(pots)
