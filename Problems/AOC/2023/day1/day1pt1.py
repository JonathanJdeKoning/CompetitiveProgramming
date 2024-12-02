ans = 0
with open("input.txt", "r") as file:
    for line in file.readlines():
        dig = [x for x in line if x.isdigit()]
        ans += int(f"{dig[0]}{dig[-1]}")
print(ans)