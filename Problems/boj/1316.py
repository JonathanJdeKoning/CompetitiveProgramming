from itertools import groupby
good = 0
for _ in range(int(input())):
    word = input()
    seen = set()
    groups = [list(k) for k, v in groupby(word)]
    for group in groups:
        if group[0] in seen: break
        else:
            seen.add(group[0])
    else:
        good += 1
print(good)
