"""
ID: jj720461 
LANG: PYTHON3
TASK: transform 
"""
import sys
sys.stdin = open("transform.in", "r")
n = int(input())

mat = [tuple(list(input())) for _ in range(n)]
targ = [tuple(list(input())) for _ in range(n)]
ninety = list(zip(*mat[::-1]))
oneeighty = list(zip(*ninety[::-1]))
twoseventy = list(zip(*oneeighty[::-1]))

ans = 7
if ninety == targ:
    ans = 1
elif oneeighty == targ:
    ans=2
elif twoseventy == targ:
    ans = 3
elif [tuple(x[::-1]) for x in mat] == targ:
    ans = 4
elif [tuple(x[::-1]) for x in ninety] == targ or [tuple(x[::-1]) for x in oneeighty] == targ or [tuple(x[::-1]) for x in twoseventy] == targ:
    ans = 5
elif mat==targ:
    ans = 6
else:
    ans = 7
with open("transform.out", "w") as out:
    out.write(str(ans)+"\n")


