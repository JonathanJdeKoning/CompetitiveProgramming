for _ in range(int(input())):
    length = int(input())
    seen = set()
    total = 0
    for c in input():
        if c in seen:
            total += 1
        else:
            total += 2
            seen.add(c)
    print(total)
