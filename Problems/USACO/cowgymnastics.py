k,n = map(int, input().split())
pairs =set()

first = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        pairs.add((first[i], first[j]))


for _ in range(k-1):
    res = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            pair = (res[i],res[j])
            rev = (res[j], res[i])
            if pair not in pairs:
                pairs.discard(pair)
            if rev in pairs:
                pairs.discard(rev)

print(len(pairs))
