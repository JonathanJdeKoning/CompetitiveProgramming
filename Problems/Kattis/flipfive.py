from collections import deque
from copy import deepcopy
directions = [(-1,0),(0,1),(1,0),(0,-1)]
def encode(board):
    binary = []
    for row in board:
        for cell in row:
            binary.append(str(int(cell != ".")))
    return int("".join(binary), 2)

def decode(num):
    binary = bin(num)[2:].zfill(9)
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            if binary[j+(3*i)] == "0":
                row.append(".")
            else:
                row.append("*")
        board.append(row)
    return board

def swap(c):
    if c == ".":
        return "*"
    else:
        return "."

def solve():
    mat = [list(input()) for _ in range(3)]
    seek = encode(mat)
    steps = -1
    q = deque([0])
    seen = set()
    while q:
        steps += 1
        for _ in range(len(q)):
            currNum = q.popleft()
            if currNum in seen: continue
            seen.add(currNum)
            if currNum == seek:
                return steps
            currBoard = decode(currNum)
            

            for i in range(3):
                for j in range(3):
                    newBoard = deepcopy(currBoard)
                    newBoard[i][j] = swap(newBoard[i][j])
                    for dy, dx in directions:
                        ny, nx = i+dy, j+dx
                        if min(ny,nx) == -1 or ny==3 or nx==3: continue
                        newBoard[ny][nx] = swap(newBoard[ny][nx])
                    newNum = encode(newBoard)
                    if newNum not in seen:
                        q.append(newNum)
                    
for _ in range(int(input())):
    print(solve())
