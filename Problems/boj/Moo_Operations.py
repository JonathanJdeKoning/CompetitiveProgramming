n = int(input())
for _ in range(n):
    s = input()
    edits = len(s)-3
    if "MOO" in s: print(edits);continue
    if "MO" in s[:-1]: print(edits+1); continue
    if "OO" in s[1:]: print(edits+1);continue
    if "O" in s[1:-1]: print(edits+2);continue
    print(-1)
