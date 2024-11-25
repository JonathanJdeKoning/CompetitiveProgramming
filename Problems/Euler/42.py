from words import words
ans = 0
tri = set([(x*(x+1))//2 for x in range(10000)])

for word in words:
    s = sum([ord(x)-64 for x in word])
    if s in tri: ans += 1

print(ans)