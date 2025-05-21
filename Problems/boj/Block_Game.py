from collections import defaultdict
N = int(input())
boards = []
for _ in range(N):
    a,b = input().split()
    boards.append((a,b))
need = defaultdict(int)
for c in "abcdefghijklmnopqrstuvwxyz":
    for board in boards:
        a,b = board
        need[c] += max(a.count(c), b.count(c))

for c in "abcdefghijklmnopqrstuvwxyz":
    print(need[c])