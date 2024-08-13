n = int(input())
def fib(n):
    if n < 2 : return abs(n-1)
    return fib(n-1) + fib(n-2)
print(fib(n))
