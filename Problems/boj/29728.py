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
from collections import deque

a = deque([])

for i in range(1,n+1):
    if not is_prime(i):
        a.append("B")
    else:
        if a[-1]=="B":
            a.pop()
            a.append("S")
            a.append("S")
        else:
            a.append("S")
    a = deque(reversed(a))
    print(a)
    print(a.count("B"), a.count("S"))
