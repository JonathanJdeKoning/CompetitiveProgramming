mat = []
with open("blank.txt", "r") as file:
    lines = [x.strip() for x in file.readlines()]
from day10pt1 import blank
print(blank)
charmap = {
    ".":[[".",".","."],
         [".",".","."],
         [".",".","."]],
    "-":[[".",".","."],
         ["#","#","#"],
         [".",".","."]],
    "|":[[".","#","."],
         [".","#","."],
         [".","#","."]],
    "L":[[".","#","."],
         [".","#","#"],
         [".",".","."]],
    "F":[[".",".","."],
         [".","#","#"],
         [".","#","."]],
    "7":[[".",".","."],
         ["#","#","."],
         [".","#","."]],
    "J":[[".","#","."],
         ["#","#","."],
         [".",".","."]],
    "S":[[".","#","."],
         [".","#","#"],
         [".",".","."]],
}



for line in lines:
    mat.append([charmap[c] for c in line])

out = ""
for i, line in enumerate(mat):
    rows = [block[0] for block in line]
    for row in rows:
        out += "".join(row)
    out +="\n"

    rows = [block[1] for block in line]
    for row in rows:
        out += "".join(row)
    out +="\n"
    
    rows = [block[2] for block in line]
    for row in rows:
        out += "".join(row)
    out +="\n"
print(out)
test = out.split("\n")
test = [list(x) for x in test]
test = test[:-1]

#for row in test:
#    print(row)
#print(test)
#print()
for i in range(len(test)):
    for j in range(len(test)):
        if test[i][j] == ".":
            test[i][j] = 0
        else:
            test[i][j] = 255
#for row in test:
#    print(row)
from PIL import Image
import numpy as np
test = np.asarray(dtype=np.int8, a=test)
#for row in test:
#    print(row)
i = Image.fromarray(test, mode="L")
i.save("test.png")


