n, qs = map(int, input().split())

a = list(map(int, input().split()))

pos = a.count(1)
neg = a.count(-1)

for _ in range(qs):
    l, r = map(int, )

    diff = (r-l)+1

    if diff%2==1:
        print(0)
        continue

    if pos >= diff//2 and neg >= diff//2:
        print(1)

