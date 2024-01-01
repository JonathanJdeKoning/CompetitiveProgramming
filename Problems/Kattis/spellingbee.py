word = input()
must = word[0]
words = int(input())
for i in range(words):
    bad = False
    new = input()
    if not (len(new) > 3):
        continue
    if must not in new:
        continue
    for c in new:
        if c not in word:
            bad = True
            break
    if not bad:
        print(new)

