n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
for row in range(n):
    for i, num in enumerate(triangle[row]):
        best = num
        if i!=0:
            best = max(best,num+triangle[row-1][i-1])
        if i != row:
            best = max(best,num+triangle[row-1][i])
        
        triangle[row][i] = best
print(max(triangle[-1]))


