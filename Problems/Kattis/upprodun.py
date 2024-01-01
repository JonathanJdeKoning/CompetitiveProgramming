import math
rooms = int(input())
teams = int(input())

inevery = int(math.floor(teams / rooms))
teamsleft = teams % rooms

output = []

for i in range(rooms):
    output.append("*"*inevery)

for i in range(teamsleft):
    output[i] += "*"

print("\n".join(output))