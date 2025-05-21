n = int(input())
h = list(map(int, input().split()))
left = 0
right = abs(h[1] - h[0])
for i in range(2, len(h)):
    left, right = right, min(right + abs(h[i]-h[i-1]), left + abs(h[i]-h[i-2]) )
    
print(right)
