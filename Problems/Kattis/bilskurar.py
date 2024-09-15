n = int(input())

h = list(map(int, input().split()))
g = list(map(int, input().split()))

uH = set()
uG = set()
ans = 0
for i in range(len(h)):
    currH = h[i]
    currG = g[i]
    
    uH.add(currH)
    uG.add(currG)

    if currH in uG:
        ans += (len(uH) + len(uG))-2

    if currG in uH:
        ans += (len(uH) + len(uG))-2

print(ans)

