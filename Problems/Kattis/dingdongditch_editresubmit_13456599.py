N, K = map(int, input().split())
houses = sorted(map(int, input().split()))
pref = [0]
tot = 0
for house in houses:
    tot += house
    pref.append(tot)

qs = list(map(int, input().split()))

for q in qs:
    print(pref[q])