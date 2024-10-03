mat = []
myKing = None
hisKing = None
myRook = None
for i in range(8):
    row = list(input())
    for j in range(8):
        if row[j] == "K":
            myKing = (i,j)
        elif row[j] == "k":
            hisKing = (i,j)
        elif row[j] == "R":
            myRook = (i,j)

if hisKing[0] not in [0,7]: exit(print("No"))
if hisKing[1] not in [0,7]: exit(print("No"))

if abs