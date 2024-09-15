from collections import deque

N, K = map(int, input().split())

A = deque(list(map(int, input().split())))

A.rotate(-K)

print(" ".join(map(str, A)))

