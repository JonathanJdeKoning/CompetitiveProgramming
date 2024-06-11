def is_prime(n):
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

import sys
n,m = map(int, input().split())

for x in range(n,m+1):
    if is_prime(x):
        sys.stdout.write(str(x)+"\n")
