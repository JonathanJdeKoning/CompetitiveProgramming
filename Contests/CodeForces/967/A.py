from collections import Counter
def solve():
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    mx = max(freq.values())
    return len(a) - mx


for _ in range(int(input())):
    print(solve())
