for _ in range(int(input())):
    numstores = int(input())
    stores = sorted(list(map(int, input().split())))
    print(2*(stores[-1]-stores[0]))
    