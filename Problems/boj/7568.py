people = []
for _ in range(int(input())):
    people.append(tuple(map(int, input().split())))
out = []
for i, (height, weight) in enumerate(people):
    rank = 1
    for j, (otherH, otherW) in enumerate(people):
        if j==i: continue
        if otherH > height and otherW> weight:
            rank += 1
    out.append(rank)

print(" ".join(map(str, out)))
