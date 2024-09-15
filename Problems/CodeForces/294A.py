n = int(input())
wires =[0]
wires.extend(list(map(int, input().split())))
wires.extend([0])

m = int(input())

for _ in range(m):
    xWire, xBird = map(int, input().split())

    numBirds = wires[xWire]
    toLeft, toRight = xBird-1, numBirds-xBird

    wires[xWire] = 0
    wires[xWire-1] += toLeft
    wires[xWire+1] += toRight

print("\n".join(map(str, wires[1:-1])))
