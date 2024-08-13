"""
ID: jj720461 
LANG: PYTHON3
TASK: beads 
"""
import sys
sys.stdin = open("beads.in", "r")
n  = int(input())
s = input()
s= s+s+s

mx = 0
for i in range(1,len(s)):
    right =0 
    left = 0
    rdef = s[i]
    ldef = s[i-1]
    for r in range(i, len(s)):
        if rdef == "w":
            if s[r] != "w": rdef = s[r]
            right += 1
        else: 
            if s[r] == rdef or s[r] == "w":
                right += 1
            else:
                break
    
    for l in range(i-1, -1,-1):
        if ldef == "w":
            if s[l] != "w": ldef = s[l]
            left += 1
        else:
            if s[l] == ldef or s[l] == "w":
                left += 1
            else:
                break
    mx = max(mx, right+left)

mx = min(mx, n)

with open("beads.out", "w") as file:
    file.write(str(mx)+"\n")



