"""
ID: jj720461
LANG: PYTHON3
TASK: gift1
"""
import sys
sys.stdin = open("gift1.in", "r")
    
n = int(input())
peeplist =[]
peeps = {}
for _ in range(n):
    peep = input()
    peeplist.append(peep)
    peeps[peep] = 0
peepinit = {}
for _ in range(n):
    giver = input()
    amount, numGetters = map(int, input().split())
    peepinit[giver] = amount
    peeps[giver] += amount
    if numGetters != 0:
        each = amount//numGetters
    for _ in range(numGetters):
        peeps[input()] += each
        peeps[giver] -= each

with open("gift1.out", "w") as out:
    for peep in peeplist:
        out.write(peep + " "+str(peeps[peep] - peepinit[peep])+"\n")
