people, budget, hotels, weeks = list(map(int, input().split()))
minprice = 999999999999
for _ in range(hotels):
    price = int(input())
    nights = list(map(int, input().split()))
    hotelprice = -1
    for night in nights:
        if night < people or (price*people) > budget:
            continue
        hotelprice = price*people
    if hotelprice < minprice and hotelprice!=-1:
        minprice = hotelprice

if minprice == 999999999999:
    print("stay home")
else:
    print(minprice)
