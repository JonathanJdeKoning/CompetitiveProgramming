from collections import Counter
n,m  = map(int, input().split())
a = list(map(int, input().split()))
c = Counter(a)
for i in range(1,m+1):
    print(c[i])
