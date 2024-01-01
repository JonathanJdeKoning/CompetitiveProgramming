h, w = list(map(int, input().split()))

seen = []
field = []
for i in range(h):
    field.append(input())

x = 0
y = 0
moves = 0
lost = False
out = False
while True:
    if moves > 100000:
        lost = True
        break
    if y < 0 or x < 0:
        out = True
        break

    try:
        op = field[y][x]
    except:
        out = True
        break

    if op == "S":
        y+=1
    elif op == "N":
        y-=1
    elif op == "E":
        x+= 1
    elif op == "W":
        x -=1
    elif op == "T":
        break
    moves += 1

if lost:
    print("Lost")
elif out:
    print("Out")
else:
    print(moves)
