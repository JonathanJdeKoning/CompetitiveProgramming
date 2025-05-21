from graphlib import TopologicalSorter
from collections import defaultdict

values = {}
parents = defaultdict(list)
ops = {}
with open("day24.in", "r") as file:
    for line in file.readlines():
        if line.strip() == "": continue
        if ":" in line:
            wire, value = line.strip().split(": ")
            values[wire] = int(value)
        else:
            a, op , b, arrow, c = line.strip().split()
            
            parents[c].append(a)
            parents[c].append(b)
            ops[c] = op
ts = TopologicalSorter(parents)
order = list(ts.static_order())

for wire in order:
    if wire in values: continue
    mom, dad = parents[wire]
    position = ops[wire]

    if position == "AND":
        values[wire] = values[mom] & values[dad]
    elif position == "OR":
        values[wire] = values[mom] | values[dad]
    elif position == "XOR":
        values[wire] = values[mom] ^ values[dad]

zs = {int(k[1:]):v for k,v in values.items() if k[0] == "z"}
binary = [str(v) for k,v in sorted(zs.items())][::-1]
print(int("".join(binary), 2))