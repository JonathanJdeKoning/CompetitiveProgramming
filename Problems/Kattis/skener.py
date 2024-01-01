h,w, nh, nw = list(map(int, input().split()))

matrix = []

for i in range(h):
    matrix.append(input())

new = []

for row in matrix:
    newstr = ""
    for c in row:
        newstr += c*nw
    
    for i in range(nh):
        new.append(newstr)

for row in new:
    print(row)
