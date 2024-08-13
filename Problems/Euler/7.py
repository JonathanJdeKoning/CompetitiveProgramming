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

x = 3
c = 2
while True:
    x+=2
    if is_prime(x):
        c +=1

    if c ==10001:
        print(x)
        break
