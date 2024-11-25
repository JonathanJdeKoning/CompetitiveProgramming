from collections import Counter
def solve(enc, org):
    orgFQ = Counter(org)

    l= 0
    r= len(org)-1

    base = Counter(enc[l:r+1])

    while True:
        if base == orgFQ: return "YES"
        #print(f"{base=}")
        #print(f"{orgFQ=}")
        #print()
        if r == len(enc) - 1: return "NO"
        base[enc[l]] -= 1
        l += 1
        r += 1
        base[enc[r]] += 1

for _ in range(int(input())):
    enc = input()
    org = input()

    print(solve(enc, org))
   