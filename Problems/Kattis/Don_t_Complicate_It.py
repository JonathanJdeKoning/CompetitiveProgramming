s = input().replace(" ","")
ans = 0
curr = 1

while s:
    x = s.count("()")
    s = s.replace("()","")
    ans += curr*x
    curr += 1
print(ans)