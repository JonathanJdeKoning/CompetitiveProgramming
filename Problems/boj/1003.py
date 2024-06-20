from functools import cache
@cache
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

for _ in range(int(input())):
    n = int(input())
    if n == 0: print(1,0)
    else:
        print(fib(n-1),fib(n))
