nums = []
mx = 0
best = None
from math import log10, floor
with open("base_exp.txt", "r") as file:
    for i, line in enumerate(file.readlines(), start=1):
        b,p = line.strip().split(",")
        b = int(b)
        p = int(p)
        nums.append((floor(1+p*log10(b)),b,p,i))
nums.sort()

print(nums[-1])
