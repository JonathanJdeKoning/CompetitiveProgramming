numbits, numqs = map(int, input().split())

bits = [0]*numbits

for _ in range(numqs):
    data = input().split()
    if data[0] == "F":
        pos = int(data[1])-1
        bits[pos] = abs(bits[pos]-1)
    elif data[0] == "C":
        l = int(data[1])
        r = int(data[2])

        print(bits[l-1:r].count(1))
