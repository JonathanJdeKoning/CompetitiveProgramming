for tc in range(int(input())):
    x,y = list(map(int, input().replace(","," ").split()))
    print(max(x,y))