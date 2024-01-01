fights = int(input())
total = 0
for fight in range(fights):
    fightstr = input()
    if "CD" not in fightstr:
        total += 1
print(total)