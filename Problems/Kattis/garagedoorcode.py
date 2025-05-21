from itertools import combinations
K, N = list(map(int, input().replace(","," ").split()))
codes = [list(input()) for _ in range(N)]

poss = set(list(combinations(codes[0], K)))

for code in codes[1:]:
    poss = poss.intersection(set(list(combinations(code, K))))

print(len(poss))

for k in sorted(poss):
    print("".join(k))