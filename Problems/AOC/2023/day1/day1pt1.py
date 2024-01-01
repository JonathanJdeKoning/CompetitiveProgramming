sum= 0
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        newline = [x for x in line if x.isdigit()]
        sum+= int(newline[0]+newline[-1])
print(sum)
