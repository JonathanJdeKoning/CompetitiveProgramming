for _ in range(int(input())):
    x1, y1, f1, x2, y2, f2 = list(map(int, input().split()))
    ans = f1+f2 + abs(x1-x2) + abs(y1-y2)
    print(ans)