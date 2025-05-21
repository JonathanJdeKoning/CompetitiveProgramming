from itertools import groupby
mod = 1000000007
N =int(input())
for _ in range(N):
    ans = 1
    s = input().strip("?")
    if "?" not in s:
        print(1)
        continue
    poss = set(list(s))
    poss.discard("?")
    groups = []

    for k, v in groupby(s):
        groups.append((k, len(list(v))))

    for i, (k, v) in enumerate(groups):
        if k == "?":
            left = groups[i-1][0]
            right = groups[i+1][0]
            if left == right:
                continue
            else:
                ans *= (v+1)
    print(ans%mod)