N = int(input())
A = list(map(int, input().replace(","," ").split()))
zeros = A.count(0)
ones = A.count(1)
ans = 0
for num in A:
    if num == 1:
        zeros += 1
        ones -= 1
    else:
        zeros -= 1
        ones += 1
    ans = max(ans, ones)
print(ans)


