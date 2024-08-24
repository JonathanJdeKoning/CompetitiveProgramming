s = input()
t = input()

curr = 0

for c in t:
    if c == s[curr]:
        curr += 1
print(curr+1)
