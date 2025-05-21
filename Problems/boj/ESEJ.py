ans = 0
N = int(input())
for _ in range(N):
    s = input()
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        else:
            top = stack[-1]
            if c != top:
                stack.append(c)
            else:
                stack.pop()
    if not stack:
        ans +=1
print(ans)