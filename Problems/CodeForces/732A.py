price, coin = map(int, input().split())

x = 1
curr = price
while curr%10 != coin and curr%10 != 0:
    curr+= price
    x += 1

print(x)
