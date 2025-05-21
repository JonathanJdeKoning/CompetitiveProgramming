ee = {54:19, 9:34, 40:64, 90:48, 67:86, 99:77}
square = 1

while True:
    roll = int(input())
    if roll == 0:
        exit(print("You Quit!"))
    if square + roll <= 100:
        square = ee.get(roll+square, roll+square)
    print(f"You are now on square {square}")
    if square == 100:
        exit(print("You Win!"))


