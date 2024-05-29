for _ in range(int(input())):
    s,t = input().split()
    mn = min(len(s), len(t))
    out = []
    for i in range(mn):
        out.append(s[i])
        out.append(t[i])
    out.append(s[mn:])
    out.append(t[mn:])
    print("".join(out))
        
