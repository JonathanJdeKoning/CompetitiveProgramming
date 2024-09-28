import sys
input = sys.stdin.readline

N = int(input())
basePref = [0]
sqPref = [0]
baseCurr = 0
sqCurr = 0
for _ in range(N):
    num = int(input())
    baseCurr+= num
    sqCurr += num**2
    basePref.append(baseCurr)
    sqPref.append(sqCurr)

mx = 0

for i in range(N+1):
    mx = max(mx, sqPref[i]*(basePref[-1]-basePref[i]))

print(mx)

