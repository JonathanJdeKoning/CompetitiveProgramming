from copy import copy
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    right = list(range(1,N+1))[::-1]
    ans = []
    for num in A:
        if num != right[-1]:
            ans.append(right.pop())
        else:
            x = right.pop()
            ans.append(right.pop())
            right.append(x)
    print(" ".join(map(str, ans)))

