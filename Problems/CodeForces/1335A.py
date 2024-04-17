for _ in range(int(input())):
    n = int(input())
    a = n/2

    if a.is_integer():
        print(int(a)-1)
    else:
        print(int(a//1))
