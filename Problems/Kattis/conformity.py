classdict = {}
for i in range(int(input())):
    classes = "".join([str(x) for x in sorted(list(map(int, input().split())))])

    if classes not in classdict:
        classdict[classes] = 1
    else:
        classdict[classes] += 1

vals = list(classdict.values())
max = max(vals)
print(vals.count(max)*max)