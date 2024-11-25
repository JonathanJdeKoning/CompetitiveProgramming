for _ in range(int(input())):
    x,y = list(map(int, input().split()))
    if y!=x and y!=x-2:
        print("No Number")
        continue
    if x%2==0:
        print(x+y)
    else:
        print(x+y-1)