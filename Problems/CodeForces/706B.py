from bisect import bisect_right
def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i
    return 0
n = int(input())
a= sorted(map(int, input().split()))

nq = int(input())

for _ in range(nq):
    q = int(input())
    print(f"{find_le(a, q)}")


