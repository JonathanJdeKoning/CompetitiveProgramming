price, perf, warprice = list(map(int, input().split()))
comprat = perf//price

print(3*(warprice*comprat))