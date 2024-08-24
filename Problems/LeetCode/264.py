from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

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

ugly = []
n = int(input())

curr = 0
while True:
    curr += 1
    bad = False
    pfs = filter(is_prime, factors(curr))
    for pf in pfs:
        if pf not in {2,3,5}:
            bad = True
            break
    if not bad:
        ugly.append(curr)
        if len(ugly) == n: print(ugly[-1])
