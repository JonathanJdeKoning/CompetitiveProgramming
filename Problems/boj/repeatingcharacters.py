for _ in range(int(input())):
    n, chars = input().split()
    n = int(n)
    out = []
    for c in chars:
        out.append(c*n)
    print("".join(out))
