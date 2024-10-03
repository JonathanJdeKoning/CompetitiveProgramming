n = int(input())

def ans(n):
    if n == 1:
        print(1,3)
        return
    if n == 2:
        print(1, 2)
        print(2, 3)
        print(1, 3)
    if n == 3:
        print(1, 3)
        print(1, 2)
        print(3, 2)
        print(1, 3)
        print(2, 1)
        print(2, 3)
        print(1, 3)