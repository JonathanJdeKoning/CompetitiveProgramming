for _ in range(int(input())):
    n = int(input())
    s = bin(n)[2:].zfill(32)
    print(int(s[::-1], 2))
