n = int(input())
s = list(input())
req = n//2


stand, sit = 0,0

for c in s:
    if c == "x":
        sit += 1
    else:
        stand += 1
change = "x"
if sit > req:
    change = "X"

x = max(sit, stand) - req
print(x)
for i,c  in enumerate(s):
    if x == 0: break
    if c != change:
        s[i] = change
        x -= 1
print("".join(s))

