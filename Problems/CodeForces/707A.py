R, C = map(int, input().split())
bad = False
for _ in range(R):
    row = input().split()
    if len([x for x in row if x not in ["B", "W", "G"]])!= 0:
        bad = True
        break

if bad:
    print("#Color")
else:
    print("#Black&White")
