from itertools import combinations_with_replacement
n,m = map(int, input().split())
combs = combinations_with_replacement(list(range(1,n+1)), m)
for comb in list(combs):
    print(" ".join(map(str, comb)))
