from itertools import permutations

def is_prime(n):
    if n < 2: 
        return False
    if n % 2 == 0:             
        return n == 2
    k = 3
    while k*k <= n:
        if n % k == 0:
            return False
        k += 2
    return True

n = ["1","2","3","4","5","6","7"][::-1]
i = 0
for perm in permutations(n):
    if perm[-1] == "2": 
        continue
    print(perm)
    if is_prime(int("".join(perm))):
        print(perm)
        break
