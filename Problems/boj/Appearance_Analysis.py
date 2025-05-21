N, M, K = list(map(int, input().replace(","," ").split()))
heir = list(map(int, input().replace(","," ").split()))
skip = set()
order = [None]*N
for _ in range(K):
    cow, pos = list(map(int, input().replace(","," ").split()))
    order[pos-1] = cow
    skip.add(cow)


if 