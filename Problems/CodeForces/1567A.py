for tc in range(int(input())):
    N = int(input())
    s = input()
    ans = []
    for c in s:
        if c == "D":
            ans.append("U")
        elif c == "U":
            ans.append("D")
        else:
            ans.append(c)
    print("".join(ans))