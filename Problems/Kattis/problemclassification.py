types = int(input())
from collections import defaultdict
triggers = {}
for _ in range(types):
    data = input().split()
    triggers[data[0]] = data[2:]
words = defaultdict(int)
while True:
    try:
        line = input()
        for word in line.split():
            words[word] += 1
    except EOFError:
        break
mx = 0
out = []
for trigger, pops in triggers.items():
    total = 0
    for pop in pops:
        total += words[pop]
    if total > mx:
        mx = total
        out = [trigger]
    elif total == mx:
        out.append(trigger)
print("\n".join(sorted(out)))
