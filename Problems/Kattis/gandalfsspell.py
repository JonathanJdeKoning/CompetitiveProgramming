s = input()
words = input().split()
used = []
mapping = {}
bad = False
for i,c in enumerate(s):
    try:
        curr = words[i]
    except:
        bad = True
        break
    if c not in mapping:
        if words[i] in used:
            bad = True
            break
        else:
            mapping[c] = words[i]
            used.append(words[i])
    else:
        if mapping[c] != words[i]:
            bad = True
            break
        else:
            continue
if len(s) != len(words):
    bad = True
print(not bad)

