password, s = input().split()

curr = 0
bad = password[1:]
yippee = True
for c in s:
    if c in bad and c!=  password[curr]:
        yippee = False
        break
    if c == password[curr]:
        curr += 1
        bad = password[curr+1:]
        if curr == len(password):
            break

if curr < len(password):
    yippee = False
if yippee:
    print("PASS")
else:
    print("FAIL")

