from collections import defaultdict
times = defaultdict(int)
for _ in range(int(input())):
    times[(tuple(map(int, input().split())))] += 1

mx = max(list(times.values()))
print(mx)
