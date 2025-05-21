for tc in range(int(input())):
    s = input()
    if len(set(list(s))) == 1:
        print(-1)
    else:
        print(len(s) - 1)