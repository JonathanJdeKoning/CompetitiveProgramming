num = input()
matrix = []
for c in num:
    matrix.append(list(bin(int(c))[2:].zfill(4).replace("1", "*").replace("0",".")))

matrix = list(zip(*matrix[::-1]))

newmatrix = []
for row in matrix:
    newmatrix.append(row[::-1])


output = ""
for row in newmatrix:
    for idx, item in enumerate(row):
        output += item
        if idx !=3:
            output += " "
        if idx == 1: output += "  "
        
    output += "\n"
    
print(output[:-1])
