from functools import cache
N = int(input())

ans = []
def move(f, t):
    print(f"Move disc from {f} to {t}")
    pass

def moveVia(f,v,t):
    move(f,v)
    move(v,t)

@cache
def hanoi(n, f, h, t):
    if n == 0: return
    hanoi(n-1, f, t, h)
    move(f,t)
    hanoi(n-1,h,f,t)
hanoi(25, 1, 2, 3)
