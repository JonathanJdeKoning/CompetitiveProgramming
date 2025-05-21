from math import log2, floor, ceil
N = int(input())
for _ in range(N):
    n = int(input())
    baseSum = ((n)*(n+1))//2

    highestPower = 2**floor(log2(n))
    print(baseSum - 2*(highestPower*2-1))
