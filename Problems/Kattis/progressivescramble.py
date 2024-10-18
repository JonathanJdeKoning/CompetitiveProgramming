trans = {k:ord(k)-96 for k in "abcdefghijklmnopqrstuvwxyz"}
trans[" "] = 0
back = {v:k for k,v in trans.items()}
def encode(s):
    new = [trans[s[0]]]
    for c in s[1:]:
        new.append((trans[c]+new[-1])%27)
    return "".join([back[x] for x in new])

def decode(s):
    new = [trans[x] for x in s]
    curr = new[0]
    out = [back[new[0]]]

    for c in new[1:]:
        for i in range(27):
            if (curr+i)%27 == c:
                curr += i
                out.append(back[i])

    return "".join(out)


N = int(input())
for _ in range(N):
    data = input()
    s = data[2:]
    op = data[0]

    if op == "e":
        print(encode(s))
    else:
        print(decode(s))