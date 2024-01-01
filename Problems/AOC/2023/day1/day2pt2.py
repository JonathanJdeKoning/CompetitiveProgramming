rep = {
    "one":"o1e",
    "two":"t2o",
    "three": "t3e",
    "four":"f4r",
    "five":"f5e",
    "six":"s6x",
    "seven":"s7n",
    "eight":"e8t",
    "nine":"n9e"
}

sum= 0
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        for key, val in rep.items():
            line = line.replace(key, val)
        newline = [x for x in line if x.isdigit()]
        sum+= int(newline[0]+newline[-1])
print(sum)
