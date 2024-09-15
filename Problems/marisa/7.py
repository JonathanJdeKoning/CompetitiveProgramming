from collections import Counter

a = list(map(int, input().split()))

fq = Counter(a)

for k, v in fq.items():
    if v in [1,3]:
        print(k)
