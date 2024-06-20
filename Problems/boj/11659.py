n, qs = map(int, input().split())
nums = list(map(int, input().split()))

pref = [0]
tot = 0
for num in nums:
    tot += num
    pref.append(tot)

for q in range(qs):
    s, e= map(int, input().split())

    print(pref[e] - pref[s-1])
