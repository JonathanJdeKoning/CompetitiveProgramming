s = input()
import re

maxi = -1
curr = s[0]
currlen = 1

if s.count(curr) >=3:
    maxi = 1

for c in s[1:]:
    if currlen > maxi:
        if len(re.findall(f"(?={c*currlen})", s)) >= 3:
            maxi = currlen
    if c == curr:
        currlen+=1
        
    else:
        curr = c
        currlen = 1

print(maxi)
