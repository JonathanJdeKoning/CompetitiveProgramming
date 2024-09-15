tones = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#","A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
from collections import defaultdict
keys = defaultdict(list)

for i in range(12):
    keys[tones[i]].append(tones[i])
    keys[tones[i]].append(tones[i+2])
    keys[tones[i]].append(tones[i+4])
    keys[tones[i]].append(tones[i+5])
    keys[tones[i]].append(tones[i+7])
    keys[tones[i]].append(tones[i+9])
    keys[tones[i]].append(tones[i+11])

n = int(input())
notes = set(input().split())

poss = []
for k,v in keys.items():
    for note in notes:
        if note not in v:
            break
    else:
        poss.append(k)
    continue
if not poss: print("none")
else:
    print(" ".join(sorted(poss)))
