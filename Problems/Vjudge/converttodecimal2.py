for _ in range(int(input())):
    n = int(input())
    c = bin(n).count("1")
    print(int("1"*c, 2))
