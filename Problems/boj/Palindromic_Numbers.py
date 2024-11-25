def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    neg = False
    if n < 0:
        n = -n
        neg = True
    while n:
        digits.append(int(n % b))
        n //= b
    if neg: digits.append("-")
    return digits[::-1]
for _ in range(int(input())):
    n = int(input())
    for b in range(2, 65):
        x = numberToBase(n, b)
        if x == x[::-1]:
            print(1)
            break
    else:
        print(0)