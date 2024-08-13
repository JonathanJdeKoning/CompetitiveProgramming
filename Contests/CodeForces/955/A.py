def solve():
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    if (a1>b1 and a2<b2) or (b1>a1 and b2<a2):
        return("NO")
    else:
        return("YES")
for _ in range(int(input())):
    print(solve())

