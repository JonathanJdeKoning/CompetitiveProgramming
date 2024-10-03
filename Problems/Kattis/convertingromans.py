N = int(input())
m = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for _ in range(N):
    stack = []

    s = input()
    ans = 0
    for c in s:
        val = m[c]
        if not stack:
            stack.append(val)
            continue

        if stack[-1] < val:
            while stack and stack[-1] < val:
                ans -= stack.pop()
        stack.append(val)
    print(sum(stack)+ans)