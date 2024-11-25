N = int(input())
mp = {}
for _ in range(N):
    c, pref = input().split()
    mp[pref] = c

out = []
buff = []
s = input()
for c in s:
    buff.append(c)
    t = "".join(buff)
    if t in mp:
        out.append(mp[t])
        buff = []
print("".join(out))