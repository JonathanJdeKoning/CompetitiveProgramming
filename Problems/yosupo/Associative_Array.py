from collections import defaultdict
N = int(input())
mp = defaultdict(int)
for _ in range(N):
    data = input().split()
    if len(data) == 3:
        mp[data[1]] = data[2]
    else:
        print(mp[data[1]])