"""
ID: jj720461 
LANG: PYTHON3
TASK: dualpal
"""
import sys
sys.stdin = open("dualpal.in", "r")

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    neg = False
    if n < 0:
        n = -n
        neg = True
    while n:
        digits.append(int(n % b))
        n //= b
    if neg: digits.append("-")
    return "".join(map(str,digits[::-1]))

n,s = map(int, input().split())
out = []
while True:
    s += 1
    bases = [numberToBase(s, i) for i in range(2,11)]
    if len([x for x in bases if x==x[::-1]]) >=2:
        out.append(str(s))
    if len(out)==n: break
with open("dualpal.out", "w") as file:
    for ans in out:
        file.write(ans+"\n")

