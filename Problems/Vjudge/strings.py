s = input()
t = input()
print(len(s), len(t))
print(s+t)
s,t = t[0]+s[1:], s[0]+t[1:]
print(s, t)
