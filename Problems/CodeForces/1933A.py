for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().replace(","," ").split()))
    print(sum([abs(x) for x in a]))