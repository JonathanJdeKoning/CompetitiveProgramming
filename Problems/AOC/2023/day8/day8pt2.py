from collections import defaultdict
inst = ""
with open("input.txt", "r") as file:
    lines = [x.strip() for x in file.readlines()]
inst = lines[0]
inst = inst*999999

nodes = {}

for line in lines[2:]:

    name, turns = line.split(" = ")
    turns = turns.split(", ")
    left = turns[0][1:]
    right = turns[1][:-1]
    
    nodes[name] = (left, right)

from math import lcm
nums = []
for one in [x for x in nodes.keys() if x.endswith("A")]:
    curr = one
    counter = 0
    while True:
        turn = inst[counter]

        if turn == "R":
            curr = nodes[curr][1]
        elif turn == "L":
            curr = nodes[curr][0]
        counter+=1
        if curr.endswith("Z"):
            break
    nums.append(counter)
print(lcm(*nums))
