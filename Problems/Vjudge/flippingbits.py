for _ in range(int(input())):
    n = int(input())
    s = bin(n)[2:].zfill(32)
    out = []
    for c in s:
        if c == "0":
            out.append("1")
        else:
            out.append("0")
    s = "".join(out)
    res = int(s, 2)
    print(res)
