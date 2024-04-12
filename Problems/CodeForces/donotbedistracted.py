from itertools import groupby
def solve():
    input()
    seen = set()
    for c in [k for k,v in groupby(input())]:
        if c in seen:
            return "NO"
        seen.add(c)
    return "YES"


if __name__ == "__main__":
    for _ in range(int(input())):
        print(solve())
