coinCount, n = map(int, input().split())

coins = []
for _ in range(coinCount):
    coins.append(int(input()))

count = 0
while n != 0:
    best = coins.pop()
    res = n//best
    count += res
    n -= best*res
print(count)
