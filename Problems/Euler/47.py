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
def dist(n):
    f = factors(n)
    p = len([x for x in f if is_prime(x)])
    return p


n = {}
curr = 1
while True:
    if curr%100 = 0: print(curr)
    n[curr] = n.get(curr, dist(curr))
    n[curr+1] = n.get(curr+1, dist(curr+1))
    n[curr+2] = n.get(curr+2, dist(curr+2))
    n[curr+3] = n.get(curr+3, dist(curr+3))

    if n[curr] == 4 and n[curr+1] ==4 and n[curr+2] == 4 and n[curr+3] == 4:
        print(curr)
        break
    curr += 1



