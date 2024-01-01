num = int(input())
drink = input()

if num != 1:
    for i in range(num,2,-1):
        print(f"{i} bottles of {drink} on the wall, {i} bottles of {drink}.\nTake one down, pass it around, {i-1} bottles of {drink} on the wall.\n")


    print(f"2 bottles of {drink} on the wall, 2 bottles of {drink}.\nTake one down, pass it around, 1 bottle of {drink} on the wall.\n")

print(f"1 bottle of {drink} on the wall, 1 bottle of {drink}.\nTake it down, pass it around, no more bottles of {drink}.")
