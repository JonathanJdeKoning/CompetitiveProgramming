rep = {"1":"7",
       "2":"6",
       "3":"5",
       "4":"4",
       "5":"3",
       "6":"2",
       "7":"1",
       "8":"0",
       "a":"0",
       "b":"1",
       "c":"2",
       "d":"3",
       "e":"4",
       "f":"5",
       "g":"6",
       "h":"7"}

white = input().split(": ")[1].split(",")
black = input().split(": ")[1].split(",")


for i, pos in enumerate(white):
    new = ""
    for c in pos:
        try:
            new += rep[c]
        except:
            new+= c
    white[i] = new

for i, pos in enumerate(black):
    new = ""
    for c in pos:
        try:
            new += rep[c]
        except:
            new+= c
    black[i] = new
black = [x.lower() for x in black]

white = ["P"+x if len(x)==2 else x for x in white]
black = ["p"+x if len(x)==2 else x for x in black]

board = [[""]*8 for _ in range(8)]


for piece in black:
    try:
        board[int(piece[2])][int(piece[1])] = piece[0]
    except:
        pass

for piece in white:
    try:
        board[int(piece[2])][int(piece[1])] = piece[0]
    except:
        pass

for row in range(8):
    for col in range(8):
        string = board[row][col]

        if string == "":
            if (row + col)%2 == 0: 
                board[row][col] = "..."
            else:
                board[row][col] = ":::"
        else:
            if (row + col) %2 == 0:
                board[row][col] = f".{string}."
            else:
                board[row][col] = f":{string}:"
import math
for i in range(17):
    if i % 2 == 0:
        print("+---+---+---+---+---+---+---+---+")
    else:
        out = "|"

        for piece in board[int(math.floor(i/2))]:
            out+= piece + "|"
        print(out)

