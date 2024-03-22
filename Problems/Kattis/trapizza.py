import math

d = int(input())

a = int(input())
b = int(input())
h= int(input())

circle = math.pi*(d/2)**2

trap = h*((a+b)/2)

if circle > trap:
    print("Mahjong!")
if trap > circle:
    print("Trapizza!")
if circle == trap:
    print("Jafn storar!")
