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
out = [x for x in range(1, int(input())+1) if is_prime(x)]
print(" ".join([str(x) for x in out]))
