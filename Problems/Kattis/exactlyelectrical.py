x, y = list(map(int, input().split()))
a,b = list(map(int, input().split()))

dist = abs(x-a) + abs(y-b)
charge = int(input())
if dist > charge:
    print("N")
else:   
    if dist%2 == charge%2:
        print("Y")
    else:
        print("N")
