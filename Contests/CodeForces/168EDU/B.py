def solve():
    n = int(input())
    top = input()
    bot = input()
    tot = 0
    for i in range(1, n-1):
        if top[i] == "." and bot[i] == ".":
            if bot[i-1] == "x" and bot[i+1] == "x" and top[i+1] != "x" and top[i-1] != "x":
                tot += 1
            if top[i-1] == "x" and top[i+1] == "x" and bot[i+1] != "x" and bot[i-1] != "x":
                tot += 1
    return tot
for _ in range(int(input())):
    print(solve())
