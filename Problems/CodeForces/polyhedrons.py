shapes = {
    "T":4,
    "C":6,
    "O":8,
    "D":12,
    "I":20
}

total = 0
for _ in range(int(input())):
    shape = input()[0]
    total += shapes[shape]
print(total)
