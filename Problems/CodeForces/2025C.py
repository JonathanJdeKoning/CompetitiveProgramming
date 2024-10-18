from collections import Counter
import itertools
for _ in range(int(input())):
    N,K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    fq = Counter(A)
    G = sorted(fq.items())
    ans = 0
    l =0 
    r = 0