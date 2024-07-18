from itertools import permutations
while True:
    k,*nums = list(map(int, input().split()))
    if k==0: break
    perms = permutations(nums, 6)
    for perm in sorted(set([tuple(sorted(list(x))) for x in list(perms)])):
        print(" ".join(map(str, perm)))
    print()

