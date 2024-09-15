for _ in range(int(input())):
    n,x,y = map(int, input().split())


    a = list(map(int, input().split()))
    new = []
    for num in a:
        new.append((num%x, num%y))
    print(new)

