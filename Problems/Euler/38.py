curr = 0
mx = 123456789
while True:
    curr += 1
    ans = []
    used = set()
    mul = 1
    bad = False
    while True:
        v = curr*mul
        digs = [x for x in str(v)]
        for d in digs:
            if d == "0":
                bad = True
                break
            if d not in used:
                used.add(d)
            else:
                bad=True
                break
        else:
            ans.extend(digs)
            mul += 1
            if len(used) == 9:
                mx = max(mx, int("".join(ans)))
                print(mx)
        if bad:
            break
