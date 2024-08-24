def solve():
    n = int(input())
    if n%2==0: return(-1)
    out = []

    for i in range(n-1, 1, -2):
        out.append(i)
    for i in range(1, n+1, 2):
        out.append(i)

    return " ".join(map(str, out))



for _ in range(int(input())):
    print(solve())
