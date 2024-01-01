mat = []
with open("input.txt", "r") as file:
    lines = [x.split() for x in file.readlines()]
    for line in lines:
        mat.append(list(line[0]))
mat = list(zip(*mat[::-1]))
new = []
for row in mat:
    new.append("".join(row))
for row in new:
    print(row)

sum = 0
for i, row in enumerate(new):
    for j, rock in enumerate(row):
        if rock == "O":
            load = 0
            ahead = new[i][j+1:]
            if "#" not in ahead:
                load = len(row)-ahead.count("O")
            else:
                aheadidx = ahead.index("#")
                rockidx = aheadidx+j+1
                
                ahead = new[i][j+1:rockidx]
                load = rockidx-ahead.count("O")
            sum += load
print(sum)
