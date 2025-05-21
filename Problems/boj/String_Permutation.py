from itertools import permutations
N = int(input())
for tc in range(N):
    print(f"Case # {tc+1}:")
    s = list(input())
    for perm in permutations(s):
        print("".join(perm))

