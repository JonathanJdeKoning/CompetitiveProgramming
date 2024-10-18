N = int(input())
ans = 1
for i in range(1,1001):
    curr = N
    for j in range(9):
        if curr%i == 0:
            curr//=i
        else:
            break
    else: ans = i

print(ans)