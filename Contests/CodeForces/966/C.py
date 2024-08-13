for _ in range(int(input())):
    n = int(input())
    temp = list(map(int, input().split()))
    seen = {}
    new = []
    curr = 0
    for x in temp:
        if x not in seen:
            new.append(curr)
            seen[x] = curr
            curr += 1
        else:
            new.append(seen[x])
    m = int(input())
    for _ in range(m):
        chars = {}
        res = []
        s = input()
        wordcurr = 0
        for c in s:
            if c not in chars:
                res.append(wordcurr)
                chars[c] = wordcurr
                wordcurr += 1
            else:
                res.append(chars[c])

        if new==res:
            print("YES")
        else:
            print("NO")
        




