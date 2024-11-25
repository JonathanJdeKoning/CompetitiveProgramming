
import math
import sys
sys.set_int_max_str_digits(10**6)

def numFactorialDigits(n): 
    if (n < 0):  return 0; 
    if (n <= 1): return 1; 
    x = ((n * math.log10(n / math.e) + 
              math.log10(2 * math.pi * n) / 2.0)); 
    return math.floor(x) + 1;

nonUnique = {
    "720":6,
    "120":5,
    "6":3,
    "2":2,
    "1":1
}

n = input()
if n in nonUnique: exit(print(nonUnique[n]))

low = 0
high = 205030

while low < high:
    mid = (low+high)//2
    
    if numFactorialDigits(mid) >= len(n):
        high = mid
    else:
        low = mid+1

print(low)