s = input()
mn = len(s)
old = s

for i in range(len(s)-1):
    for j in range(i, len(s)+1):
        sub = s[i:j]
        s = s.replace(sub, "M")
        mn =min(mn, len(s) + j-i)
        s = old

print(mn)