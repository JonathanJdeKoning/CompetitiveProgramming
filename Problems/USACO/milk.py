"""
ID: jj720461
LANG: PYTHON3
TASK: milk
"""
import sys
sys.stdin = open("milk.in","r")
need, nFarmers = map(int, input().split())

milks = []
for _ in range(nFarmers):
    price, avail = map(int, input().split())
    milks.append((price, avail))
milks.sort()
cost = 0
for price, avail in milks:
    take = min(avail, need)
    need -= take
    cost += take*price
    if need ==0: break

with open("milk.out", "w") as file:
    file.write(str(cost)+"\n")
