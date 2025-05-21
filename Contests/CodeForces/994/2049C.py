def solve():
    n,x,y = list(map(int, input().replace(","," ").split()))
    if n == 3: return "0 1 2"

    base = []
    for i in range(n):
        base.append(i%2)
    if n%2 == 1:
        base[-1] = 2
    x -= 1
    y -= 1

    if abs(x-y) ==1 or sorted([x,y]) == [0,n-1]:
        return " ".join(map(str, base ))

    dx = base[x]
    dy = base[y]
    if n%2 == 0:
        if dx == dy:
            base[x] = 2
        return " ".join(map(str, base ))

    if dy != dx:
        return " ".join(map(str, base ))
    
    if y == 0 or x == 0:
        base = base[::-1]
        return " ".join(map(str, base))

    base[min(x,y)] = 2
    return " ".join(map(str, base))

    



for tc in range(int(input())):
    print(solve()) 