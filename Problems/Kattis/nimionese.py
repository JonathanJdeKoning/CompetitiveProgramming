hard = ["b","c","d","g","k","n","p","t"]
ends = ["a", "o", "u"]
words = input().split()

ans = []
for word in words:
    syllbs = word.split("-")
    out = []
    start = word[0]
    dists = [abs(ord(start.lower()) - ord(x)) for x in hard]
    new = hard[dists.index(min(dists))]
    if start.isupper():
        out.append(new.upper())
    else:
        out.append(new.lower())
    out.append(syllbs[0][1:])

    for syllb in syllbs[1:]:
        for c in syllb:
            if c in hard:
                if c.islower():
                    out.append(new.lower())
                else:
                    out.append(new.upper())
            else:
                out.append(c)
    out = [x for x in out if x]
    last = out[-1][-1]
    if last.lower() in hard:
        dists = [abs(ord(last.lower()) - ord(x)) for x in ends]
        new = ends[dists.index(min(dists))]
        out.append(new+"h")
    ans.append("".join(out).replace("-",""))

print(" ".join(ans))


