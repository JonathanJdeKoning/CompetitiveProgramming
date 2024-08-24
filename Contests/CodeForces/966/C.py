for _ in range(int(input())):
    n = int(input())
    temp = list(map(int, input().split()))
    m = int(input())

    for _ in range(m):
        s = input()
        if len(s) != len(temp):
            print("NO")
            continue
        
        ch = {}
        seen = set()
        for i, c in enumerate(s):
            if c not in ch:
                rep = temp[i]
                if rep in seen:
                    print("NO")
                    break
                else:
                    ch[c] = rep
                    seen.add(rep)
            else:
                rep = ch[c]
                if temp[i] != rep:
                    print("NO")
                    break
        else:
            print("YES")
        continue




