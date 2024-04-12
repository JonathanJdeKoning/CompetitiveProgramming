n = int(input())

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

x = 4
y = n-4

while True:
    if not is_prime(x) and not is_prime(y):
        print(x,y)
        break
    x += 1
    y-= 1

