def solve():
    s = input()
    t = input()
    out = []
    curr = 0
    for i,c in enumerate(s):
        if c == t[curr] or c=="?":
            if c=="?":
                out.append(t[curr])
            else:
                out.append(c)

            curr += 1

            if curr == len(t):
                print("YES")
                return "".join(out) + s[i+1:].replace("?","a")
        else:
            out.append(c)
    return "NO"
for _ in range(int(input())):
    print(solve())
