N = int(input())
rocks = list(map(int, input().split()))
s = sorted(rocks)
less = {}

for i, rock in enumerate(s):
    less[rock] = i

print(" ".join(map(str, [less[x] for x in rocks])))
