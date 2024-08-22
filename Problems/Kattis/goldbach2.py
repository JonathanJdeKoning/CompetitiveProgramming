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
qs = []
for _ in range(n):
    qs.append(int(input()))
mx = max(qs)

primes = []
for i in range(1,mx+1):
    if is_prime(i):
        primes.append(i)

primeset = set(primes)
for q in qs:
    reps = []
    mid = q//2+1
    for prime in primes:
        if prime >= mid: break
        
        if q-prime in primeset:
            reps.append((prime, q-prime))

    print(f"{q} has {len(reps)} representation(s)")

    for a,b in reps:
        print(f"{a}+{b}")
    print()


