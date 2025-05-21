s = input().replace("::", ":@@@@:")
groups = [g.zfill(4) for g in s.split(":") if g]
s = ":".join(groups)
N = s.count(":")
if N == 8:
    print(s)
else:
    s = s.replace("@@@@", ":".join(["0000"]*(8-N)))
    print(s)