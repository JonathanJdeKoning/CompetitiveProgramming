def solve():
    N = int(input())
    s = list(input())
    while True:
        if len(s) == 1:
            return 1
        if not s:
            return 0

        a = s.pop()
        s = s[::-1]
        b = s.pop()
        if a == b:
            return len(s) + 2

for tc in range(int(input())):
    print(solve())