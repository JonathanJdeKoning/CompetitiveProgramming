for tc in range(int(input())):
    a,b = list(map(int, input().replace(","," ").split()))
    if (a+b)%2 == 0:
        print("Bob")
    else:
        print("Alice")


    