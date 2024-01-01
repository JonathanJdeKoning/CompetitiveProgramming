n = int(input())
a = set([int(x) for x in input().split()])
b = set([int(x) for x in range(1, n + 1)])

print(next(iter(b-a)))
