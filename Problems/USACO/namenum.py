"""
ID: jj720461 
LANG: PYTHON3
TASK: namenum
"""
import sys
sys.stdin = open("namenum.in")

d = {"A":2,"B":2,"C":2,"D":3,"E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,"O":6,"P":7,"R":7,"S":7,"T":8,"U":8,"V":8,"W":9,"X":9,"Y":9}


def nameToNums(name):
    out = []
    for c in name:
        if c in "QZ": return []
        out.append(d[c])
    return out

nums = list(map(int, list(input())))
ans = []
with open("dict.txt", "r") as file:
    for name in file.readlines():
        name = name.strip()
        namenums = nameToNums(name)
        if namenums == nums:
            ans.append(name)

ans.sort()
with open("namenum.out", "w") as out:
    if ans ==[]:
        out.write("NONE\n")
    else:
        for name in ans:
            out.write(name+"\n")
    
