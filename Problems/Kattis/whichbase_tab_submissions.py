from copy import copy
for _ in range(int(input())):
    k, n = map(int, input().split())
    n = list(str(n))

    out = []
    for base in [8,16]:
        ans = 0
        curr = 0
        new = copy(n)
        if base == 8 and "9" in new: out.append(ans);continue
        while new:
            ans += int(new.pop())*(base**curr)
            curr += 1
        out.append(ans)
    print(k, out[0], "".join(n), out[1])