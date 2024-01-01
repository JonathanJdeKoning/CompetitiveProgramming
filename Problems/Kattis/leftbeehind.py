
while True:
    a,b = list(map(int, input().split()))

    if a + b == 13:
        print("Never speak again.")
        continue
    if a > b:
        print("To the convention.")
        continue
    if a < b:
        print("Left beehind.")
        continue
    if a ==0 and b == 0:
        break

    print("Undecided.")