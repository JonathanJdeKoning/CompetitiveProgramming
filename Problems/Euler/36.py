ans = 0
for i in range(1000000):
    s = str(i)
    if s == s[::-1] and bin(i)[2:] == bin(i)[2:][::-1]:
        ans += i

print(ans)