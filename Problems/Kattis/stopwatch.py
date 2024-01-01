presses = int(input())

total = 0
if presses%2 == 1:
    print("still running")
else:
    for i in range(presses//2):
        a = int(input())
        b = int(input())
        
        total += b-a
    print(total)
        