data = []

while True:
    line = input().split()
    if line == ["-1"]:
        break
    data.append(line)

mainpoints = sum([int(x[0]) for x in data if x[2]== "right"])
solved = [x[1] for x in data if x[2] =="right"]

penpoints = sum([20 for x in data if x[1] in solved and x[2]!="right"])
totalpoints = penpoints+mainpoints
print(len(solved), totalpoints)


