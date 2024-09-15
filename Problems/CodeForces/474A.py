s = "qwertyuiopasdfghjkl;zxcvbnm,./"

x = 1 if input()=="L" else -1

out = []
for c in input():
    out.append(s[s.find(c)+x])
print("".join(out))
