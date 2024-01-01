total = 0

string = input()

total += len([x for x in string[::3] if x != "P"])
total += len([x for x in string[1::3] if x != "E"])
total += len([x for x in string[2::3] if x != "R"])
print(total)