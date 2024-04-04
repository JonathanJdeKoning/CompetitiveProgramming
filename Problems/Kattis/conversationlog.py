from collections import defaultdict
nummessages = int(input())
playas = defaultdict(list)
wordses = defaultdict(int)
for _ in range(nummessages):
    data = input().split()
    name = data[0]
    words = data[1:]
    playas[name].extend(words)
    for word in words:
        wordses[word] += 1

setts = list(playas.values())
start = set(setts[0])
for c in setts[1:]:
    start = start.intersection(c)
if not start:
    print("ALL CLEAR")
start = list(start)
print("\n".join(sorted(start, key=lambda x:(-wordses[x], x))))
