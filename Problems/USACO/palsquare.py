"""
ID: jj720461 
LANG: PYTHON3
TASK: palsquare
"""
import sys
sys.stdin = open("palsquare.in", "r")

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    digits = list(map(lambda x:chr(x+55) if x >=10 else x, digits))
    return "".join(map(str,digits[::-1]))

n = int(input())
with open("palsquare.out", "w") as file:
    for i in range(1,301):
        sq = numberToBase(i**2, n)
        new = numberToBase(i, n)
        if sq == sq[::-1]:
            file.write(f"{new} {sq}\n")
