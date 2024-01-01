teams = int(input())

teamdict = {}
for i in range(teams):
    name, section = input().split()

    if name not in teamdict:
        teamdict[name] = [section]
    else:
        teamdict[name].append(section)

count = 0
for name, sections in teamdict.items():
    if count != 12:
        print(name + " " + sections[0])
        count += 1