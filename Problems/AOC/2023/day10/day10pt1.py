mat = []
blank = []
for i in range(140):
    line = []
    for j in range(140):
        line.append(".")
    blank.append(line)
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        mat.append(line.strip())
#S is at 30,72
y, x = 30, 73
curr = mat[y][x]
prev = [0,1]
total = 0
while curr != "S":
    total += 1 
    curr = mat[y][x]
    if curr == "-":
        blank[y][x] = "-"
        x+=prev[1]
    elif curr == "|":
        blank[y][x] = "|"
        y+=prev[0]
    elif curr == "L":
        blank[y][x] = "L"
        if prev == [0,-1]:
            y-=1
            prev = [-1,0]
        elif prev == [1,0]:
            x+=1
            prev = [0,1]
    elif curr == "J":
        blank[y][x] = "J"
        if prev == [1,0]:
            x-=1
            prev = [0,-1]
        elif prev == [0,1]:
            y-=1
            prev = [-1,0]
    elif curr == "7":
        blank[y][x] = "7"
        if prev == [0,1]:
            y+=1
            prev = [1,0]
        elif prev == [-1,0]:
            x-=1
            prev = [0,-1]
    elif curr == "F":
        blank[y][x] = "F"
        if prev == [-1,0]:
            x+=1
            prev = [0,1]
        elif prev == [0,-1]:
            y+=1
            prev = [1,0]
    
    print(f"{y},{x}, {curr}, {total}")
print(total/2)

out = ""

for line in blank:
    out += "".join(line)
    out += "\n"

with open("blank.txt", "w") as file:
    file.write(out)

