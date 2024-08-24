for _ in range(int(input())):
    for _ in range(3):
        row = set(list(input()))
        if "?" in row:
            print(({"A","B","C"}-row).pop())

