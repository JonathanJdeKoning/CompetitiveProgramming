def solve():
    a, b = map(int, input().split())
    ans = 999
    for c in range(a, b+1):
        ans = min(ans, (c-a)+(b-c))
    return ans


for _ in range(int(input())):
    print(solve())
