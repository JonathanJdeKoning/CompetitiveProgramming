cakeWidth = int(input())
pieces = int(input())

totalArea = 0
for piece in range(pieces):
    pieceWidth, pieceLength = list(map(int, input().split()))
    totalArea += pieceWidth*pieceLength
print(totalArea//cakeWidth)