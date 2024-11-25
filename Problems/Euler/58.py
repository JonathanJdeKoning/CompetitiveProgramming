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
from time import sleep
side = 0
curr = 1
p = 0
t = 1
while True:
    side += 2
    for _ in range(4):
        curr += side
        t += 1
        if is_prime(curr):
            p += 1
    print(p/t)
    if p/t <0.1:
        print(side+2)
        break


