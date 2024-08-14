def calc(n):
    if n == 1:
        return 3
    return 3+ (3/calc(n-1))

print(calc(4))

