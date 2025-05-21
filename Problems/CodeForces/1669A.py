for tc in range(int(input())):
    N = int(input())
    if N <= 1399:
        print("Division 4")
    elif N <= 1599:
        print("Division 3")
    elif N <= 1899:
        print("Division 2")
    else:
        print("Division 1")