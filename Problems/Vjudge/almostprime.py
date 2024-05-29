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
n = int(input())
total = 0
for i in range(1,n+1):
    prime_factors = set(filter(is_prime, factors(i)))
    prime_factors.discard(1)
    prime_factors.discard(i)
    if len(prime_factors) == 2:
        total += 1
print(total)

