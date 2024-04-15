from collections import deque
for _ in range(int(input())):
    s = input()
    out = deque([])
    at_end = True
    revme = []
    for c in s:
        if c =="]":
            out.extendleft(revme[::-1])
            revme = []
            at_end = True
            continue
        elif c == "[":
            at_end = False
            revme = []
            continue
        if c =="<":
            if at_end:
                try:
                    out.pop()
                except:pass
            else:
                try:
                    revme.pop()
                except: pass
        else:
            if at_end:
                out.append(c)
            else:
                revme.append(c)
    if revme:
        out.extendleft(revme[::-1])
    print("".join(out))
