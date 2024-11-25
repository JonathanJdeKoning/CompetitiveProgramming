from itertools import pairwise
while True:
    words = []
    bad = False
    while True:
        word = input()
        if word == "#":
            if not words: exit()
            break
        words.append(word)
    for a,b in pairwise(words):
        if len(a) != len(b): bad = True; continue
        if len([1 for x,y in zip(a,b) if x!=y]) != 1: bad=True; continue
    if bad:
        print("Incorrect")
    else:
        print("Correct")