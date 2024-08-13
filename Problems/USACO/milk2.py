"""
ID: jj720461 
LANG: PYTHON3
TASK: milk2
"""
import sys
sys.stdin = open("milk2.in", "r")

n = int(input())

intervals = []

for _ in range(n):
    s, e = map(int, input().split())
    intervals.append([s,e])

intervals.sort()
out = []
curr = intervals[0]
for interval in intervals[1:]:
    start = interval[0]
    end = interval[1]
    if start > curr[1]:
        out.append(curr)
        curr = interval
    else:
        curr[1] = max(end, curr[1])
out.append(curr)
prvE = out[0][0]
mxMilk = 0
mxNoMilk =0
for s, e in out:
    mxMilk = max(mxMilk, e-s)
    mxNoMilk = max(mxNoMilk, s-prvE)
    prvE = e

with open("milk2.out", "w") as file:
    file.write(f"{mxMilk} {mxNoMilk}\n") 

