n = int(input())
old = n
x = 0
while True:
    num = sum([int(z) for z in str(n)])
    n = int(str(n)[-1] + str(num)[-1])
    x += 1
    if n == old:
        print(x)
        break
