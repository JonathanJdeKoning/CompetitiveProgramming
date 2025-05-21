N = int(input())

ans = []
def move(f, t):
    ans.append((f,t))


def moveVia(f,v,t):
    move(f,v)
    move(v,t)

def hanoi(n, f, h, t):
    if n == 0: return
    hanoi(n-1, f, t, h)
    move(f,t)
    hanoi(n-1,h,f,t)
hanoi(N, 1, 2, 3)

print(len(ans))
for f,t in ans:
    print(f,t)