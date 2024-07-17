
n, k = map(int, input().split())
num = list(map(int, input()))
need = len(num)-k
ans = [num[0]]
for i, c in enumerate(num[1:], start=1):
    numsLeft = (n-i)-1
    moreNeeded = need-len(ans)
    while ans and c > ans[-1] and numsLeft >= moreNeeded:
        ans.pop()
        moreNeeded += 1
    if moreNeeded>0:
        ans.append(c)
        moreNeeded -= 1
print("".join(map(str,ans)))
    
