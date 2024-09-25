from math import ceil
paperWidth, paperHeight = map(int, input().split())

numChars, charWidth, charHeight = map(int, input().split())

if charWidth > paperWidth or charHeight> paperHeight: exit(print(-1))
charsPerRow = paperWidth//charWidth
charsPerCol = paperHeight//charHeight

charsPerPage = charsPerRow*charsPerCol
numPages = ceil(numChars/charsPerPage)

print(numPages)