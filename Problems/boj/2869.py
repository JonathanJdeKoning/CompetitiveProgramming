climb, slide, height = map(int, input().split())

daily = climb-slide
toWin = height-climb

from math import ceil, floor
print(ceil(toWin/daily)+1)

