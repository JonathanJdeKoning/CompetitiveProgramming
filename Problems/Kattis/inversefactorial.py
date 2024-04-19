

import math
import bisect
import sys
sys.set_int_max_str_digits(10**6)

def findDigits(n): 
    if (n < 0): 
        return 0; 
    if (n <= 1): 
        return 1; 
    x = ((n * math.log10(n / math.e) + 
              math.log10(2 * math.pi * n) /2.0)); 
    return math.floor(x) + 1;
known = {3628800: 10,
         362880: 9,
         40320:8,
         5040:7,
         720:6,
         120:5,
         24:4,
         6:3,
         2:2,
         1:1}
def solve():
    n = input()
    if int(n) in known:
        print(known[int(n)])
        return
    digits = len(n)
    poss = list(range(1, 205030))

    left = 0
    right = len(poss)

    while left < right:
        mid = (left+right)//2
        if findDigits(poss[mid]) < digits:
            left = mid+1
        elif findDigits(poss[mid]) > digits:
            right = mid
        elif findDigits(poss[mid]) ==digits:
            print(poss[mid])
            break
solve()
