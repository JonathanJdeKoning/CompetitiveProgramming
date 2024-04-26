
from math import ceil
n = int(input())
total = 0
mult = 1
needed = 2

for _ in range(n):
    note = int(input())
    if note == 0:
        needed = mult
        mult = ceil(mult/2)
        
    else:
        needed -= 1
        if needed == 0:
            if mult <8:
                mult*=2
                needed = mult*2
        total += note*mult

    print(f"TOTAL: {total}, MULT  {mult}")

print(total)
