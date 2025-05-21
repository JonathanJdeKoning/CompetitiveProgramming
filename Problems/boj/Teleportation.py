start, end, x, y = list(map(int, input().replace(","," ").split()))

one = abs(start-end)
two = abs(start-x) + abs(y-end)
three = abs(start-y) + abs(x-end)

print(min(one, two , three))