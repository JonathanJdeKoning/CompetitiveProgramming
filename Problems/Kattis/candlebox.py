diff = int(input())
rBox = int(input())
tBox = int(input())
n = rBox + tBox

rCurr = 0
tCurr = 0

rAge = 4
tAge = rAge - diff
while True:
    rCurr += rAge
    if tAge >= 3:
        tCurr += tAge
    
    if rCurr + tCurr == n:
        print(rBox - rCurr)
        break
    rAge += 1
    tAge += 1