import sys
input = sys.stdin.readline
from math import sqrt, ceil

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

def factorize(n):
    factors = []
    while True:
        for i in range(2, ceil(sqrt(n))+1):
            if n%i==0:
                n//=i
                factors.append(i)
                break
        else:
            if n != 1:
                factors.append(n)
            break
    return factors

while True:
    n = int(input().strip())
    if n == 4: break
    ans = 0

    while True:
        ans += 1
        if is_prime(n):
            print(n, ans)
            break
        
        n = sum(factorize(n))
