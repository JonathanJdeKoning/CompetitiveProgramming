n = int(input())
a = list(map(int, input().split()))

l = 0
r = len(a) -1

while True:
    left = a[l]
    right = a[r]

    if left == 1 or left == n:
        exit(print((n-l)-1))

    if right == 1 or right == n:
        exit(print(r))

    l += 1
    r -= 1

