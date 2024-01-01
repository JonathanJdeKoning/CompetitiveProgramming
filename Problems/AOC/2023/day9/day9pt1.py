with open("input.txt", "r") as file:
    lines = [list(map(int, x.strip().split())) for x in file.readlines()]

sum = 0
for line in lines:
    compute = [line]

    curr = line
    while curr.count(0) != len(curr):
        diffs = [j-i for i,j in zip(curr[:-1], curr[1:])]
        compute.append(diffs)
        curr = diffs

    newcurr = 0
    for i, comp in enumerate(compute[::-1]):
        comp.append(comp[-1]+newcurr)
        newcurr = comp[-1]
    sum += newcurr
print(sum)
