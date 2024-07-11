a = "qwertyuiop"
b = "asdfghjkl"
c = "zxcvbnm"

lookup = {}

for row, chars in enumerate([a,b,c]):
    for idx, char in enumerate(chars):
        lookup[char] = (row, idx)
for _ in range(int(input())):
    word, n = input().split()
    n = int(n)
    
    out = {}
    for _ in range(n):
        
        total = 0
        new = input()
        for newC, oldC in zip(new, word):
            tupA = lookup[newC]
            tupB = lookup[oldC]
            total += abs(tupA[0] - tupB[0])
            total += abs(tupA[1] - tupB[1])
        out[new] = total
    items = out.items()
    items = sorted(items, key=lambda x:(x[1], x[0]))
    for word, x in items:
        print(word, x)




