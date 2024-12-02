from collections import defaultdict
N,K = list(map(int, input().split()))
names = input().split()
hunter = defaultdict(int)
hunter[names[0]] = 1
cheaters = set()
for _ in range(K):
    start, _, end = input().split()
    if not hunter[start]:
        cheaters.add(start)
    hunter[end] = 1
    hunter[start] = 0

print(len(cheaters))
print(" ".join(sorted(cheaters)))
