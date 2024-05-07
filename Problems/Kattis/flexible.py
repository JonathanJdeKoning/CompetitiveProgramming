w,p = map(int, input().split())
ls = [0] + list(map(int, input().split())) + [w]

out = []
for i, left in enumerate(ls):
    for j, right in enumerate(ls):
        if i>=j: continue
        out.append(right-left)
out = set(out)
out.discard(0)
print(" ".join([str(x) for x in sorted(list(out))]))

