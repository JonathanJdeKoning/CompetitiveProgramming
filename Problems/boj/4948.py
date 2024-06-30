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

qs = []
while True:
    n = int(input())
    if n ==0:break
    qs.append(n)

primes = set()

for i in range(2*max(qs)+1):
    if is_prime(i):
        primes.add(i)


for q in qs:
    total = 0
    for i in range(q+1,1+(2*q)):
        if i in primes:
            total += 1
    print(total)
