lines = int(input())

history = []
names = []
for line in range(lines):
    command, name = input().split()
    if command == "entry":
        command = 1
    if command == "exit":
        command = 0
    history.append([name, command])
    names.append(name)

status = {}
for name in names:
    status[name] = 0

for thingy in history:
    output = thingy[0] + " "
    if thingy[1] == 0:
        output += "exited"
    if thingy[1] == 1:
        output += "entered"
    


    if status[thingy[0]] == thingy[1]:
        output += " (ANOMALY)"
    status[thingy[0]] = thingy[1]


    print(output)