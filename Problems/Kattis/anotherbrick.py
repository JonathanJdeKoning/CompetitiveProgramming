layers, width, numbricks = list(map(int, input().split()))
bricks = list(map(int, input().split()))
bad = False

count = 0

for i in range(layers):
    left = width
    brick = bricks[count]
    while left != 0:
        left -= brick
        count += 1
        try:
            brick = bricks[count]
        except:
            bad = False
        if left < 0:
            print("NO")
            bad = True
            break
    if bad:
        break

if not bad:
    print("YES")
