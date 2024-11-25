N,K = list(map(int, input().split()))
drinks = [input() for _ in range(N)]
from collections import defaultdict
cust = defaultdict(int)
for _ in range(K):
    s = input()
    print(drinks[cust[s]])
    cust[s] += 1