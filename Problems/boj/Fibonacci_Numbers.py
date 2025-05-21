fib = []
x = 0
y = 1
for _ in range(50):
    fib.append(y)
    x, y = y, x+y
fib = fib[::-1]
for _ in range(int(input())):
    N = int(input())
    ans = []
    for num in fib:
        if num <= N:
            ans.append(num)
            N -= num
    print(*ans[::-1])