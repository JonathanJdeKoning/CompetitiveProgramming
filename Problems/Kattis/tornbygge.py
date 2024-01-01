numbricks = int(input())

bricks = list(map(int, input().split()))

towers = 1

curr = bricks[0]

for brick in bricks[1:]:
    if brick > curr:
        towers += 1
    curr = brick 
print(towers)