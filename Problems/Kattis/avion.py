blimps = []
for i in range(5):
    blimp = input()
    if "FBI" in blimp:
        blimps.append(str(i+1))

if len(blimps) == 0: 
    print("HE GOT AWAY!")
else: print(" ".join(blimps))
