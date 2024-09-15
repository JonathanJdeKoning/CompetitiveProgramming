n = input()
ans = 0
for c in n:
    if c.isdigit():
        ans += int(c)
print(ans)
