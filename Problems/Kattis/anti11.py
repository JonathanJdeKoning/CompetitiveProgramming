def fib(n):
    x = 1
    y = 2
    for _ in range(n):
        x,y = y, x+y
    return x

for _ in range(int(input())):
    print(fib(int(input()))%(10**9+7))
