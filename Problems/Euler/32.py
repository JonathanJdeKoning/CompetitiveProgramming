from itertools import permutations
ans = set()

A = ["1","2","3","4","5","6","7","8","9"]

for perm in permutations(A):
    for i in range(1,7):
        for j in range(i+1, 9):
            a = int("".join(perm[:i]))
            b = int("".join(perm[i:j]))
            c = int("".join(perm[j:]))

            if a*b == c and c not in ans:
                ans.add(c)
                print(a,b,c)



print(sum(ans))