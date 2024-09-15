n = int(input())
s = input()
t = input()
ans = 0
for i in range(n):
    a = int(s[i])
    b = int(t[i])

    diff = abs(a-b)
    
    ans += min(diff, abs(diff-10))

print(ans)

