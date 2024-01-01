rows = int(input())

mytable = []

for i in range(rows):
    mytable.append(list(map(int, input().split())))

mydata = []

for row in range(rows):
    for col in range(rows):
        if mytable[row][col] != -1:
            mydata.append([row+1, col+1, mytable[row][col]])

datalength = len(mydata)

mydata = sorted(mydata)

print(datalength)

for row in mydata:
    row = [str(x) for x in row]
    print (" ".join(row))