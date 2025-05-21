n = int(input())

ans = []
x,y = 0,1
for _ in range(60):
    x,y = y, x+y
    ans.append(x%10)
print(ans[n%60])