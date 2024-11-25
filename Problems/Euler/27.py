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
def f(n,a,b):
    return n**2+a*n+b
mx =0
bestA = None
bestB = None
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while True:
            val = f(n,a,b)
            if is_prime(val):
                n += 1
            else:
                if n > mx:
                    mx = n
                    bestA =a
                    bestB = b
                break
print(f"{bestA=}, {bestB=}")
print(bestA*bestB)

