from collections import defaultdict
def prime_sieve(n):
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend([3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1])
    return res

def digitSum(n):
    return sum([int(c) for c in str(n)])

P = set([str(p) for p in prime_list(100000) if p > 9999])
allOdd = set(list(filter(lambda p: all([int(c)%2==1 for c in p]), P)))
dig0 = defaultdict(set)
dig1 = defaultdict(set)
dig2 = defaultdict(set)
dig3 = defaultdict(set)
dig4 = defaultdict(set)
sums = defaultdict(set)
for p in P:
    sums[digitSum(p)].add(p)
    dig0[p[0]].add(p)
    dig1[p[1]].add(p)
    dig2[p[2]].add(p)
    dig3[p[3]].add(p)
    dig4[p[4]].add(p)
