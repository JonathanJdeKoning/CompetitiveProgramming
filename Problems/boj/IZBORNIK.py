N = int(input())
seen = set()
for _ in range(N):
    s = input().split()
    for i,word in enumerate(s):
        if word[0].lower() not in seen:
            seen.add(word[0].lower())
            s[i] = f"[{word[0]}]{word[1:]}"
            print(" ".join(s))
            break
    else:
        s = " ".join(s)
        for i,c in enumerate(s):
            if c == " ": continue
            if c.lower() not in seen:
                print(f"{s[:i]}[{s[i]}]{s[i+1:]}")
                seen.add(c.lower())
                break
        else:
            print(s)
    continue
