key = input()
zoom = len(key)

y = 0
x = 0


for i, c in enumerate(key):
    y*=2
    x*=2
    if c == "1":
        x += 1
    elif c == "2":
        y += 1
    elif c == "3":
        y, x = y+1, x+1
print(zoom, x, y)

