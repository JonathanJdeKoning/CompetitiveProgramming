matrix = []
symbs = "`~!@#$%^&()/\\}{[];:'\",<>?=+-_"
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    linelength = len(lines[0])
    matrix.append("."*(linelength+2))
    for line in lines:
        for symb in symbs:
            line = line.replace(symb, ".")
        matrix.append(f".{line}.")
    matrix.append("."*(linelength+2))

curr = ""
myrange = [0, 0]
num = 0
gears = {}
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        pos = matrix[i][j]
        if pos == "*":
            gears[str(i)+","+str(j)] = []

print("\n".join(matrix))
def getGear(matrix, row, start, end):
    gearRow = -1
    gearCol = -1

    left = matrix[row][start-1]
    right = matrix[row][end+1]
    if left == "*":
        gearRow = row
        gearCol = start-1

    if right == "*":
        gearRow = row
        gearCol = end+1
    
    uprange = matrix[row-1][start-1:end+2]
    downrange = matrix[row+1][start-1:end+2]
    
    for i, c in enumerate(uprange):
        if c == "*":
            gearRow = row-1
            gearCol = (i+start)-1

    for i, c in enumerate(downrange):
        if c == "*":
            gearRow = row+1
            gearCol = (i+start)-1
    return gearRow, gearCol

curr = ""
start = -1
end = -1
for i, row in enumerate(matrix):
    for j, col in enumerate(matrix):
        pos = matrix[i][j]
        if pos.isdigit():
            if start == -1:
                start = j
            curr += pos
        if pos == "." or pos == "*":
            if curr != "":
                end = j-1
                num = int(curr)
                gearRow, gearCol = getGear(matrix, i, start, end)

                if gearRow != -1:
                    gears[f"{gearRow},{gearCol}"].append(num)
                start = -1
                end = -1
                curr = ""

gearsum = 0
for key, val in gears.items():
    if len(val) == 2:
        gearsum+= val[0]*val[1]
print(gearsum)
