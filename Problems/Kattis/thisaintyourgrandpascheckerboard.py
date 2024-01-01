lines = int(input())

bad = False
mat = []
for line in range(lines):
    line = input()
    linearr = list(line)
    mat.append(linearr)
    if "BBB" in line or "WWW" in line:
        bad = True
    if line.count("W") != line.count("B"):
        bad = True

rotated = list(zip(*mat[::-1]))
for row in rotated:
    line = "".join(row)
    if "BBB" in line or "WWW" in line:
        bad = True
    if line.count("W") != line.count("B"):
        bad = True
print("0") if bad else print("1")
