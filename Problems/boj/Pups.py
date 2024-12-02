for _ in range(int(input())):
    dogs, pounds, price = list(map(float, input().split()))
    ans = round(dogs*pounds*price, 2)
    print(f"${format(ans, ".2f")}")