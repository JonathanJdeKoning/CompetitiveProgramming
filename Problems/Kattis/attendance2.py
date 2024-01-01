calls = int(input())
absent = []

shouts = [input() for _ in range(calls)][::-1]
good = False
for i in range(calls):
    curr = shouts[i]
    if good == True:
        good = False
        continue
    if curr == "Present!":
        good = True
        continue
    else:
        good = False
    if not good:
        absent.append(curr)


if len(absent) == 0:
    print("No Absences")
else:
    print("\n".join(absent[::-1]))

