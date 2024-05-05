numCoins = int(input())
coins = sorted(list(map(int, input().split())), reverse=True)
tot = sum(coins)
hand = 0
for i,coin in enumerate(coins):
    tot -= coin
    hand += coin
    if hand > tot:
        print(i+1)
        break
