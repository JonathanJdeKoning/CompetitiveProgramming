for _ in range(int(input())):
    mysum, mydiff = map(int, input().split())
    if mysum < mydiff:
        print("Impossible")
        continue
    left = 0
    right = mydiff
    while True:
        if left + right == mysum:
            print(right, left)
            break
        elif left + right > mysum:
            print("Impossible")
            break
        left += 1
        right += 1
