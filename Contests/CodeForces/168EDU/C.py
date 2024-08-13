def solve():
    n = int(input())
    s = list(input())
    tot = 0
    vals = []
    open = 0
    for i, c in enumerate(s):
        if c == "(":
            open += 1
            vals.append(i)
        elif c == ")":
            open -=1
            tot += i- vals.pop()
        else:
            if open > 0 :
                s[i] = ")"
                open -= 1
                tot += i-vals.pop()
            else:
                s[i] = "("
                open += 1
                vals.append(i)
    return tot


for _ in range(int(input())):
    print(solve())
