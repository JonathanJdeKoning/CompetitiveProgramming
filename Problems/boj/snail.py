from math import floor, ceil
climb, slide, height = map(int, input().split())

gain = climb - slide

init = ceil(height/gain)
initend = gain*init
if init -((initend+slide)-climb) <= climb:
    print(init-1)
else:
    print(init)
