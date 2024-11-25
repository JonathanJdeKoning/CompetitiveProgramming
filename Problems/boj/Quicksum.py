while True:
    s = input()
    if s == "#": break
    ans = 0
    for i,c in enumerate(s,start=1):
        if c == " ": continue
        v = ord(c)-64
        ans += i*v
    print(ans)