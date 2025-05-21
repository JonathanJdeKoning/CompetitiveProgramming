N = int(input())
w, l, h = 0,0,0
if N == 1:
    w = int(input())
    l = w
    h = 3

if N == 2:
    w = int(input())
    l = int(input())
    h = 3

if N == 3:
    w = int(input())
    l = int(input())
    h = int(input())
print((w*l*h) - ((w-2)*(l-2)*(h-1)))