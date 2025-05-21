for tc in range(int(input())):
    x, k = list(map(int, input().replace(","," ").split()))
    if x % k != 0:
        print(1)
        print(x)
    else:
        print(2)
        print(x-1, 1)