mxID = 0
seats = []
with open("day5.in", "r") as file:
    for line in file.readlines():
        line = line.strip()
        x = 64
        low = 0
        high = 127
        for c in line[:-3]:
            if c == "F":
                high -= x
            else:
                low += x
            x //=2
        row = low
        low = 0
        high = 7
        x = 4
        for c in line[-3:]:
            if c == "L":
                high -= x
            else:
                low += x
            x//=2
        col = low
        myID = row*8+col
        mxID = max(mxID, myID)
        seats.append(myID)

print(mxID)
seats.sort()
for i in range(min(seats), max(seats)):
    if i+1 in seats and i-1 in seats and i not in seats:
        print(i)