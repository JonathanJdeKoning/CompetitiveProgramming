import math
people = int(input())

prices = []
for i in range(people):
    name, price = input().split()
    price = int(price)
    prices.append(price)
prices=sorted(prices)

if len(prices) %2 ==1:
    print(sum(prices[::2]))
else:
    print(sum(prices[1::2]))
